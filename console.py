#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json


class HBNBConsole(cmd.Cmd):
    """create the console prompt"""
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.storage = FileStorage()
        self.storage.reload()
        self.all_objects = self.storage.all()

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        pass

    def do_quit(self, arg):
        """quit and EOF to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit and EOF to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg.split()[0]
            class_obj = getattr(models.base_model, class_name)
            new_instance = class_obj()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.all_objects.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in self.all_objects:
            print("** no instance found **")
            return
        print(self.all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.all_objects.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in self.all_objects:
            print("** no instance found **")
            return
        del self.all_objects[key]
        self.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in self.all_objects.values()])
        elif args[0] not in self.all_objects.keys():
            print("** class doesn't exist **")
        else:
            print(
                    [str(value) for key, value in self.all_objects.items()
                        if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in self.storage.classes.keys():
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        if key not in self.all_objects:
            print("** no instance found **")
            return
        setattr(self.all_objects[key], args[2], args[3])
        self.storage.save()


if __name__ == "__main__":
    HBNBConsole().cmdloop()
