#!/usr/bin/python3


class Square:
    _Square__size = None

    def __init__(self, size=0):
        try:
            if type(size) == int:
                if size >= 0:
                    self._Square__size = size
                else:
                    raise ValueError("size must be >=0")
            else:
                raise TypeError("size must be an integer")
        except ValueError as er:
            print(er)
        except TypeError as err:
            print(err)

    def area(self):
        return self._Square__size * self._Square__size
