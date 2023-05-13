#!/usr/bin/python3
"""Module for FileStorage class.

serializes instances to a JSON file and deserializes JSON file to instances.

Typical usage example:

    storage = file_storage.FileStorage()

"""

import json

valid_classes = {"BaseModel", "User"}

# set of modules where valid_classes elements can be found
modules = {"models.base_model", "models.user"}


class FileStorage:
    """Serializes and Deserializes.

    serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path: A string containing the path to the JSON file
        __objects: A dictionary that stores of all objects by <class name>.id
    """

    __file_path = "storefile.json"
    __objects = {}

    def __init__(self) -> None:
        """Initializes the instance.
        """
        pass

    def all(self) -> dict:
        """Returns the dictionary `__objects`"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj
        # print(f"\nIn new (before saving):\n{FileStorage.__objects}\n")

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""

        store = {}

        for key, value in FileStorage.__objects.items():
            if type(value) is not dict:
                store[key] = value.to_dict()
                # it is very important that 'value' is not converted to dict
                # 'in place' using a copy was very necessary in the to_dict()
                # method
            else:
                store[key] = value

        # print(f"\nHere is the content of store before dump:\n{store}\n")
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(store, f, indent=2)
        # print(f"\nHere is the content of store after dump:\n{store}")

    def reload(self) -> None:
        """deserializes the JSON file(in __file_path) to __objects
        (only if the JSON file (__file_path) exists)"""

        try:
            # I put this here instead of the top to avoid circular imports
            from models.base_model import BaseModel
            from models.user import User
            import sys

            with open(FileStorage.__file_path, 'r') as f:
                # In order for objects not to persist even when json storage
                # file is deleted set __objects to empty
                FileStorage.__objects = {}
                temp = json.load(f)

                for key, value in temp.items():
                    class_name, obj_id = key.split('.')
                    # print(f"class name is: {class_name}\n")
                    module = ""

                    for modl in modules:
                        cls = getattr(sys.modules[modl], class_name, None)
                        if cls is not None and cls.__name__ in valid_classes:
                            # print(f"{cls} is found in {modl}\n")
                            module = modl
                            # print(f"module is {module}\n")
                            break

                    if module:
                        cls = getattr(sys.modules[module], class_name)
                        # print(f"\nFinal cls: {cls}")
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj

        except FileNotFoundError as e:
            pass
