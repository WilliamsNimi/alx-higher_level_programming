#!/usr/bin/python3


def add_integer(a, b=98):
    """ This is the add_integer function """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt", optionflags=doctest.ELLIPSIS)
