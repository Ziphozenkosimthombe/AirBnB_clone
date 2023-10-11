#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """class for HBNBCommand"""

    """custom prompt"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """enter Quit to exit the program"""
        return True

    def do_EOF(self, line):
        """enter EOF to exit the program"""
        return True

    def emptyline(self):
        """empty line will execute anything"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
