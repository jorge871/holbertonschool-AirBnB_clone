#!/usr/bin/python3
"""console for AirBNB clone"""
import cmd


class Console(cmd.Cmd):
    """create the console prompt"""
    prompt = "(hbnb) "
    pass


if __name__ == "__main__":
    Console().cmdloop()
