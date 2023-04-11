#!/usr/bin/python3


""" This is a BaseGeometry Module """
class BaseGeometry:
    """ This is the Base Geometry class """

    def area(self):
        """ This is the area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This is the type validator """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt", optionflags=ELLIPSIS)
