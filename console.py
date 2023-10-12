#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class for HBNBCommand"""

    """custom prompt"""
    prompt = '(hbnb)'
    classObjects = {}

    def do_quit(self, line):
        """enter Quit to exit the program"""
        return True

    def do_EOF(self, line):
        """enter EOF to exit the program"""
        return True

    def emptyline(self):
        """empty line will execute anything"""
        pass

    def do_create(self, line):
        """new BaseModel instance"""
        if not line:
            print('** class name missing **')
            return
        try:
            myInstance = eval(line)()
            myInstance.save()
            print(myInstance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """the string representation of an
        instance based on the class name
        and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        wordsList = line.split()
        length = len(wordsList)
        if length == 0:
            print('** class name missing **')
            return
        elif length == 1:
            print("** instance id missing **")
            return
        elif length > 2:
            print('** many arguments **')
            return
        className = wordsList[0]
        instanceId = wordsList[1]
        if className not in self.classDict:
            print("** class doesn't exist **")
            return
        classObjects = storage.all()
        key = className + "." + instanceId
        if key in classObjects:
            print(classObjects[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, line):
        """ Deletes an instance based on the class name
        and id (save the change into the JSON file). Ex:
        $ destroy BaseModel 1234-1234-1234.
        """
        wordsList = line.split()
        if wordsList == []:
            print("** class name missing **")
            return
        elif self.classDict.get(wordsList[0]):
            print("** class doesn't exist ** ")
            return
        elif len(wordsList) != 2:
            print("** instance id missing **")
            return
        classObjects = storage.all()
        key = wordsList[0] + '.' wordsList[1]
        if key in classObjects.keys():
            classObjects.pop(key)
            storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
