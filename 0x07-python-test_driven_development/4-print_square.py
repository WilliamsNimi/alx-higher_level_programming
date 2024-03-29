#!/usr/bin/python3


def print_square(size):
    """ This function prints a square with # """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt", optionflags=ELLIPSIS)
