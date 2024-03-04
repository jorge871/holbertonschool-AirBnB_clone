#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from shlex import split as sp


class HBNBConsole(cmd.Cmd):
    """create the console prompt"""
    prompt = "(hbnb) "
    model_classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }

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
            if class_name not in self.model_classes:
                print("** class doesn't exist **")
                return
            class_obj = self.model_classes[class_name]
            new_instance = class_obj()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        self.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            print(
                    [str(value) for key, value in storage.all().items()
                        if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = sp(arg)
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
        class_name = args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        if key not in self.all_objects:
            print("** no instance found **")
            return
        obj = self.model_classes[key]
        attribute_name = args[2]
        if args[2] == "my_number":
            setattr(storage.all()[key], attribute_name, int(args[3]))
        else:
            setattr(storage.all()[key], attribute_name, args[3])
        self.storage.save()


if __name__ == "__main__":
    HBNBConsole().cmdloop()
