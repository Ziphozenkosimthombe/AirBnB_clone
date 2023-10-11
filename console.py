#!/usr/bin/python3
import cmd
import inspect
import models
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Inherits Cmd"""
    prompt = '(hbnb) '

    def do_quit(self, line) ->None:
        """Quit command to exit the program
        """
        exit(1)

    def do_EOF(self, line) -> bool:
        """Return True
        """
        return True
    
    def emptyline(self) -> None:
        """Overrides emptyline in the super class so that
        an empty line + ENTER shouldn’t execute anything
        """
        pass
    
    def do_create(self, line) -> None:
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        # get all the classes defined in the base_model module
        classes = [cls for name, cls in inspect.getmembers(models.base_model, inspect.isclass)]
        # get the names of all the classes
        class_names = [cls.__name__ for cls in classes]
    
        if line is not None and len(line) !=  0:
            if line in class_names:
                instance = models.base_model.BaseModel()
                models.storage.save()
                print(instance.id)
            else:
                print("class doesn't exist")
        else:
            print('class name missing')

    def do_show(self, line):
        """"prints the string representation of an instance based
        on the class name and id
        """
        args_list = line.split()
        if len(args_list) == 2:
            models.storage.reload()
            obj = models.storage.all()
            key = args_list[0] + '.' + args_list[1]
            if key in obj:
                print(obj.get(key))
            else:
                print('no instance found')
        elif len(args_list) < 1:
            print('class name missing')
        else:
            print('instance id missing')

    def do_destroy(self, line) -> None:
        """
        Deletes an instance based on the
        class name and id (save the change into the JSON file).
        """
        args_list = line.split()
        if len(args_list) == 2:
            models.storage.reload()
            obj = models.storage.all()
            key = args_list[0] + '.' + args_list[1]
            if key in obj:
                del obj[key]
                models.storage.save()
            else:
                print('no instance found')
        elif len(args_list) < 1:
            print('class name missing')
        else:
            print('instance id missing')

    def do_all(self, line) -> None:
        """
        Prints all string representation of
        all instances based or not on the class name
            Example:
                $ all BaseModel
                $ all
        """
        pass



            


if __name__ == '__main__':
    HBNBCommand().cmdloop()