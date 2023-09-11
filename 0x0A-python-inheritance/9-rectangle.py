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


class Rectangle(BaseGeometry):
    """ This is the rectangle class """
    _Rectangle__height = None
    _Rectangle__width = None

    def __init__(self, width, height):
        """ This is the __init__ function """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__height = height
        self._Rectangle__width = width

    def area(self):
        """ This is the area function """
        return self._Rectangle__height * self._Rectangle__width

    def __repr__(self):
        """ This is the __repr__ function """
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Rectangle] {}/{}".format(width, height)

    def __str__(self):
        """ This is the __str__ function """
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Rectangle] {}/{}".format(width, height)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt", optionflags=ELLIPSIS)
