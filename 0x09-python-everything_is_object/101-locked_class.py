#!/usr/bin/python3
"""
This is the LockedClass
"""
class LockedClass:
    def __setattr__(self, __name, __value):
        """This is the dunder methos __setattr__"""
        if __name == "first_name":
            super().__setattr__(__name, __value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute'{__name}'")
