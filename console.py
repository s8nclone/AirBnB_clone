#!/usr/bin/python3
"""Console Module.

Contains the entry point of the command interpreter.

"""
import cmd
from models.base_model import BaseModel
from models import storage
from typing import Union


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter.
    """
    prompt = '(hbnb) '
    file = None

    def emptyline(self) -> bool:
        return False

    def do_quit(self, arg: str) -> bool:
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg: str) -> None:
        """End of File Command to exit the program
        """
        print()
        quit()

    def do_create(self, arg: str) -> None:
        """Creates a new instance of BaseModel and prints the id.

        Example:
            create BaseModel
        """
        ret_val = arg_splitter("create", arg)
        # print(f"return value is {ret_val}")

        if ret_val is True:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, arg: str) -> None:
        """Prints the string representation of an instance \
            based on the class name and id.

        Example:
            show BaseModel 1234-1234-1234
        """
        ret_val = arg_splitter("show", arg)

        if ret_val:
            output = find_id(ret_val)
            if output:
                print(output)

    def destroy(self, arg):
        ret_val = arg_splitter("destroy", arg)

        # if ret_val


def arg_splitter(cls: str, arg: str) -> Union[bool, str]:
    """Helper function to help split arguments (DRY)

    The arguments entered into the command interpreter are splitted
        on white spaces.

    Arguments:
        cls -> The name of the HBNBCommand method where arg_splitter is used
        arg -> The argument received from the class

    Return:
        returns True if all goes well but the id of the BaseModel instance
            where it is applicable
        returns False if entries are in complete or class does not exist
    """
    args = arg.split()

    if not args:
        print("** class name missing **")
        return False

    if args[0] != "BaseModel":
        print("** class doesn't exist **")
        return False

    if cls in {"show", "destroy", "update"}:
        if len(args) < 2:
            print("** instance id missing **")
            return False
        else:
            return args[1]

    return True


def find_id(instance_id: str) -> str:
    """Find id of a class instance (DRY)
    """
    all_objects = storage.all()
    for key, value in all_objects.items():
        cls, id = key.split(".")
        if id == instance_id:
            return value
    else:
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
