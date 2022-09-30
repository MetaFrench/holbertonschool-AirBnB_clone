#!/usr/bin/python3
"""Holberton AirBnB Project for Holberton (Console)"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for Console Commands"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered as input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
