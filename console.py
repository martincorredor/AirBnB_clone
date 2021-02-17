#!/usr/bin/python3
"""
"""
import cmd
import sys
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "\
Place": Place, "Review": Review, "State": State, "User": User}
"""


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit of my command interpreter"""
        return True

    def do_EOF(self, line):
        """Quit or "finally" my command interpreter"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
