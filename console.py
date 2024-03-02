#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import models


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new.instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            print([str(value) for value in all_objects.values()])
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            print(
                    [str(value) for key, value in all_objects.items()
                        if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(all_objects[key], args[2], args[3])
        storage.save()


if __name__ == "__main__":
    HBNBConsole().cmdloop()
