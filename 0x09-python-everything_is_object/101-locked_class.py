#!/usr/bin/python3
from typing import Any


class LockedClass:
    def __setattr__(self, __name, __value):
        if __name == "first_name":
            super().__setattr__(__name, __value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute'{__name}'")
