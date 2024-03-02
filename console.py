#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd


class HBNBConsole(cmd.Cmd):
    """create the console prompt"""
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        pass

    def do_quit(self, arg):
        """quit and EOF to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit and EOF to exit the program"""
        return True


if __name__ == "__main__":
    HBNBConsole().cmdloop()
