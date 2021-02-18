#!/usr/bin/python3
"""
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"
    modules = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit of my command interpreter"""
        return True

    def do_EOF(self, line):
        """Quit or "finally" my command interpreter"""
        print()
        return True
    
    def emptyline(self):
        """Do not execute anything\n"""
        pass
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        if line:
            args = line.split(' ')
        
            if args[0] not in self.modules:
                print("** class doesn't exist **")
            else:
                if args[0] == self.modules[0]:
                    instance = BaseModel()
                elif args[0] == self.modules[1]:
                    instance = User()
                elif args[0] == self.modules[2]:
                    instance = State()
                elif args[0] == self.modules[3]:
                    instance = Amenity()
                elif args[0] == self.modules[4]:
                    instance = Place()
                elif args[0] == self.modules[5]:
                    instance = Review()
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.modules:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(line[0], line[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[name])

    def to_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        arg = line.split(' ')
        if len(line) == 0:
            print("** class name missing **")
        elif arg[0] not in self.modules:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(line[0], line[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()

    def do_all(self, arg):
        """
         Prints all string representation of all instances
         based or not on the class name
        """
        arg = line.split(' ')
        if len(line) == 0:
            for objs in storage.all().values():
                print(objs)
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, objs in storage.all().items():
                if arg[0] in k:
                    print(storage.all()[k])

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        line = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            check_id = "{}.{}".format(line[0], line[1])
            if check_id not in storage.all().keys():
                print("** no instance found **")
            elif len(line) == 2:
                print("** attribute name missing **")
            elif len(line) == 3:
                print("** value missing **")
            else:
                cast = type(eval(line[3]))
                arg_3 = line[3].strip('"')
                setattr(storage.all()[check_id], line[2], cast(arg_3))
                storage.all()[check_id].save()

    def do_count(self, arg):
        """\n Update the number of instances of a class\n"""
        count = 0
        for k, objs in storage.all().items():
            if arg in k:
                count += 1
            print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
