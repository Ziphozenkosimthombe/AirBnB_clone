#!/usr/bin/python3
'''interprete commands'''
import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
# from models.engine.file_storage import FileStorage


class_list = {
            'BaseModel': BaseModel,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User,
            'Amenity': Amenity
            }
# get all data stored in a file
models.storage.reload()
# get the dict of contents of the file invoked above
obj = models.storage.all()


class HBNBCommand(cmd.Cmd):
    """Inherits Cmd"""

    # override the default prompt
    prompt = '(hbnb) '

    def do_quit(self, line) -> bool:
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line) -> bool:
        """Quits the console
        Returns True
        """
        print('')
        return True

    def emptyline(self) -> None:
        """Overrides emptyline in the super class so that
        an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line) -> None:
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
            Example:
                $ create BaseModel
        """
        if line is not None and len(line) != 0:
            if line in class_list:
                instance = eval(line + '()')
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, line):
        """prints the string representation of an instance based
        on the class name and id
        Arg:
            line: the argument provided alongside the command
        Examle:
            $ show BaseModel 1234-1234-1234
        Usage:
            $ show <class name> <id>
            $ <class name>.show(<id>)
        """
        args_list = line.split()
        if len(args_list) == 2:
            if args_list[0] in class_list:
                key = args_list[0] + '.' + args_list[1]
                if key in obj:
                    print(obj.get(key))
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        elif len(args_list) < 1:
            print('** class name missing **')
        else:
            print('** instance id missing **')

    def do_destroy(self, line) -> None:
        """Deletes an instance based on the\
        class name and id (save the change into the JSON file).
        Example:
            $ destroy BaseModel 1234-1234-1234
        Usage:
            $ destroy <class name> <id>
            $ <class name>.destroy(<id>)
        """
        args_list = line.split()
        if len(args_list) == 2:
            key = "{}.{}".format(args_list[0], args_list[1])
            if args_list[0] in class_list:
                if key in obj:
                    del obj[key]
                    models.storage.save()
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        elif len(args_list) < 1:
            print('** class name missing **')
        else:
            print('** instance id missing **')

    def do_all(self, line) -> None:
        """Prints all string representation of
        all instances based or not on the class name
        Example:
            $ all BaseModel
            $ all
        """

        if len(line) == 0:
            list = [str(obj.get(key)) for key in obj.keys()]
            if len(list) != 0:
                print(list)
        elif line in class_list:
            list = [str(obj.get(key)) for key in obj.keys() if line in key]
            if len(list) != 0:
                print(list)
        else:
            print('** class doesn\'t exist **')

    def do_update(self, line) -> None:
        """Updates an instance based on the class name and id by adding or \
            updating attribute (save the change into the JSON file).
        Only one attribute can  be updated at the time
        Example:
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage:
            $ update <class name> <id> <attribute name> "<attribute value>"
            $ <class name>.update(<id>, <attr name>, <attr value>)
            $ <class name>.update(<id>, <dictionary representation>)
        """
        args_list = line.split()

        if len(args_list) > 4:
            del args_list[4:]

        if len(args_list) == 0:
            print('** class name missing **')
        elif len(args_list) == 1:
            if args_list[0] not in class_list:
                print('** class doesn\'t exist ** ')
            else:
                print('** instance id missing **')
        elif len(args_list) == 2:
            if args_list[0] not in class_list:
                print('** class doesn\'t exist ** ')
            else:
                print('** attribute name missing **')
        elif len(args_list) == 3:
            if args_list[0] not in class_list:
                print('** class doesn\'t exist ** ')
            else:
                print('** value missing **')
        elif len(args_list) == 4:
            if args_list[0] not in class_list:
                print('** class doesn\'t exist ** ')
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key in obj:
                    instance = obj[key]
                    setattr(instance, args_list[2],
                            args_list[3].lstrip("\"").rstrip('\"'))
                    instance.save()
                else:
                    print('** no instance found **')

    def do_count(self, line) -> None:
        """Prints number of instances
        Example:
            $ count User
        Usage:
            $ count <class name>
        """
        if len(line) == 0:
            list = [str(obj.get(key)) for key in obj.keys()]
            print(len(list))
        elif line in class_list:
            list = [str(obj.get(key)) for key in obj.keys() if line in key]
            print(len(list))
        else:
            print('** class doesn\'t exist **')

    def default(self, line: str) -> None:
        """Handle unknown commands.
        Example:
            $ User.all()
        Usage:
            <class name>.update(<id>, <dictionary representation>)
        """
        class_name, _, fun = line.partition('.')
        command, _, param = fun.partition('(')

        if class_name in class_list and param.endswith(')'):
            if command == 'all':
                self.do_all(class_name)
            elif command == 'count':
                self.do_count(class_name)
            elif command == 'show':
                param = "{} {}".format(class_name, param.rstrip(')'))
                self.do_show(param)
            elif command == 'destroy':
                param = "{} {}".format(class_name, param.rstrip(')'))
                self.do_destroy(param)
            elif command == 'update':
                param = "{} {}".format(class_name,
                                       param.rstrip(')'))
                param_list = param.split(',')
                if param.endswith('}'):
                    # Define a regex pattern to match
                    # dictionary-like substrings
                    pattern = r'{[^{}]*}'
                    # Use re.findall() to find all occurrences of the pattern
                    matches = re.findall(pattern, param)
                    dict = eval(matches[0])
                    for key, val in dict.items():
                        arg = "{} {} {}".format(param_list[0], key, val)
                        self.do_update(arg)
                else:
                    param = "{} {} {}".format(param_list[0],
                                              param_list[1], param_list[2])
                    self.do_update(param)
            else:
                print('*** Unknown syntax: %s' % line)
        else:
            print('*** Unknown syntax: % s' % line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
