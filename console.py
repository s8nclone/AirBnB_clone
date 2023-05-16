#!/usr/bin/python3
"""Console Module.

Contains the entry point of the command interpreter.

"""
import ast
import cmd
import re
import sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from typing import Union
from models.engine.file_storage import valid_classes
from models.engine.file_storage import modules

all_objects = storage.all()


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
        class_name = arg_splitter("create", arg)
        # print(f"return value is {ret_val}")

        if class_name:
            for modl in modules:
                cls = getattr(sys.modules[modl], class_name, None)
                if cls:
                    model = cls()
                    model.save()
                    print(model.id)
                    break

    def do_show(self, arg: str) -> None:
        """Prints the string representation of an instance \
            based on the class name and id.

        Example:
            show BaseModel 1234-1234-1234
        """
        cls, obj_id = arg_splitter("show", arg)

        if obj_id:
            obj = find_instance(cls, obj_id)
            if obj:
                print(obj)

    def do_destroy(self, arg: str) -> None:
        """Deletes an instance based on the class name and id.
        """
        cls, obj_id = arg_splitter("destroy", arg)

        if obj_id:
            obj = find_instance(cls, obj_id)
            if obj:
                del all_objects[f"{obj.__class__.__name__}.{obj_id}"]
                storage.save()

    def do_all(self, arg: str) -> None:
        """Prints all string representation of all instances \
based or not on the class name.
        """
        args = arg_splitter("all", arg)

        if args:
            obj_list = []

            for obj in all_objects.values():
                obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg: str) -> None:
        """
        Updates an instance based on the class name and id

        This is done by adding or updating attribute

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        # print(f"\nType of arg_splitter return value: \
        #     {type(arg_splitter('update', arg))}\
        #         Return value is {arg_splitter('update', arg)}")
        if type(arg_splitter("update", arg)) is not bool:
            cls, id, attr_name, attr_val = arg_splitter("update", arg)

            if attr_name in {"id", "created_at", "updated_at"}:
                print(f"** can't update the {attr_name} attribute **")
            else:
                instance = all_objects[f"{cls}.{id}"]
                setattr(instance, attr_name, ast.literal_eval(attr_val))

                # make sure "updated_at" is well, up to date
                setattr(instance, "updated_at", datetime.now())
                storage.save()
            # print(f"\nInstance: {instance}")

    def default(self, line: str) -> None:
        """Called on an input line when the command prefix is not recognized.

        In this case, we check if the line has the form "<class name>.all()"
        and if so, we retrieve all instances of that class.
        """
        allowed_methods = {"all", "update", "show", "count", "destroy"}
        pattern = r"^(.+)\.(.+)\((.*)\)"

        matched = re.match(pattern, line)

        if matched:
            class_name = matched.group(1)
            class_method = matched.group(2)
            arg = matched.group(3)

            if class_name not in valid_classes:
                print("** class doesn't exist **")
                return
            elif class_method not in allowed_methods:
                print("** unknown method **")
                return
            if class_method == "all":
                objs = all_objects.values()
                filtered_objs = list(filter(
                    lambda obj: type(obj).__name__ == class_name, objs))
                print([str(obj) for obj in filtered_objs])

            elif class_method == "count":
                objs = storage.all().values()
                filtered_objs = list(filter(
                    lambda obj: type(obj).__name__ == class_name, objs))
                print(len(filtered_objs))
            elif class_method == "show":
                obj = find_instance(class_name, arg)
                if obj:
                    print(obj)
            elif class_method == "destroy":
                obj = find_instance(class_name, arg)
                if obj:
                    del all_objects[f"{obj.__class__.__name__}.{arg}"]
                    storage.save()
            elif class_method == "update":
                update_args = arg.split(", ")
                id = update_args[0]
                obj = find_instance(class_name, id)
                if not obj:
                    return
                if len(update_args < 2):
                    print("** attribute name missing **")
                elif len(update_args < 3):
                    print("** value missing **")
                attr_name = update_args[1]
                attr_val = update_args[2]

                if attr_name in {"id", "created_at", "updated_at"}:
                    # print(f"** can't update the {attr_name} attribute **")
                    pass
                else:
                    instance = all_objects[f"{class_name}.{id}"]

                    try:
                        setattr(
                            instance, attr_name, ast.literal_eval(attr_val)
                            )
                    except Exception as e:
                        setattr(instance, attr_name, attr_val)

                    # make sure "updated_at" is well, up to date
                    setattr(instance, "updated_at", datetime.now())
                    storage.save()
        else:
            super().default(line)


def arg_splitter(my_method: str, arg: str) -> Union[bool, str]:
    """Helper function to help split arguments (DRY)

    The arguments entered into the command interpreter are splitted
        on white spaces.

    Arguments:
        my_method -> The name of the HBNBCommand method where
                        arg_splitter is used
        arg -> The argument received from the class

    Return:
        returns True if all goes well but the id of the BaseModel instance
            where it is applicable
        returns False if entries are in complete or class does not exist
    """
    args = arg.split()

    if not args:
        if my_method == "all":
            return True
        print("** class name missing **")
        return False

    if args[0] not in valid_classes:
        print("** class doesn't exist **")
        return False

    if my_method in {"show", "destroy", "update"}:
        if len(args) < 2:
            print("** instance id missing **")
            return False
        elif my_method == "update":
            if len(args) > 1:
                if not find_instance(args[0], args[1]):
                    return False
                elif len(args) < 3:
                    print("** attribute name missing **")
                    return False
            if len(args) < 4:
                print("** value missing **")
                return False
            else:
                return args[0], args[1], args[2], args[3]
        else:
            return args[0], args[1]

    return args[0]


def find_instance(cls: str, instance_id: str) -> Union[BaseModel, None]:
    """Finds instance based on the id (DRY).
    """

    for key, obj in all_objects.items():
        obj_cls = key.split(".")[0]
        if obj_cls == cls and obj.id == instance_id:
            return obj
    else:
        print("** no instance found **")
    return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
