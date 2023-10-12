#!/usr/bin/python3
import cmd
import inspect
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage


class_list = {
        'BaseModel',
        'City',
        'Place',
        'Review',
        'State',
        'User',
        'Amenity'
}
# get all data stored in a file
models.storage.reload()
# get the dict of contents of the file invoked above
obj = models.storage.all()


class HBNBCommand(cmd.Cmd):
    """Inherits Cmd"""

    # override the default prompt
    prompt = '(hbnb) '

    def do_quit(self, line) -> None:
        """Quit command to exit the program
        """
        exit(1)

    def do_EOF(self, line) -> bool:
        """Return True
        """
        return True

    def emptyline(self) -> None:
        """
        Overrides emptyline in the super class so that
        an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line) -> None:
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
            Example:
                $ create BaseModel
        """
        # get all the classes defined in the base_model module
        # classes = [cls for name, cls in inspect.getmembers(
        #     models.line, inspect.isclass)]
        # # get the names of all the classes
        # class_names = [cls.__name__ for cls in classes]

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
        """
        prints the string representation of an instance based
        on the class name and id
            Examle:
                $ show BaseModel 1234-1234-1234
        """
        args_list = line.split()
        if len(args_list) == 2:
            key = args_list[0] + '.' + args_list[1]
            if key in obj:
                print(obj.get(key))
            else:
                print('** no instance found **')
        elif len(args_list) < 1:
            print('** class name missing **')
        else:
            print('** instance id missing **')

    def do_destroy(self, line) -> None:
        """
        Deletes an instance based on the
        class name and id (save the change into the JSON file).
            Example:
                $ destroy BaseModel 1234-1234-1234
        """
        args_list = line.split()
        if len(args_list) == 2:
            key = f"{args_list[0]}.{args_list[1]}"
            print(key)
            if key in obj:
                del obj[key]
                models.storage.save()
            else:
                print('** no instance found **')
        elif len(args_list) < 1:
            print('** class name missing **')
        else:
            print('** instance id missing **')

    def do_all(self, line) -> None:
        """
        Prints all string representation of
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
        """
        Updates an instance based on the class name and id by adding or \
            updating attribute (save the change into the JSON file).
        Only one attribute can  be updated at the time
            Example:
                $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args_list = line.split()
        # store all the class names from the storage file in list
        class_names = []
        for i in obj.keys():
            str = ""
            for j in range(len(i)):
                if i[j] != '.':
                    str += i[j]
                else:
                    break
            if not (str in class_names):
                class_names.append(str)
            str = ""

        if len(args_list) > 4:
            del args_list[4:]

        match len(args_list):
            case 0:
                print('** class name missing **')
            case 1:
                if not (args_list[0] in class_names):
                    print('** class doesn\'t exist ** ')
                else:
                    print('** instance id missing **')
            case 2:
                if not (args_list[0] in class_names):
                    print('** class doesn\'t exist ** ')
                else:
                    print('** attribute name missing **')
            case 3:
                if not (args_list[0] in class_names):
                    print('** class doesn\'t exist ** ')
                else:
                    print('** value missing **')
            case 4:
                if not (args_list[0] in class_names):
                    print('** class doesn\'t exist ** ')
                else:
                    key = f"{args_list[0]}.{args_list[1]}"
                    if key in obj:
                        instance = obj[key]
                        setattr(instance, args_list[2],
                                args_list[3].lstrip("\"").rstrip('\"'))
                        instance.save()
                    else:
                        print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
