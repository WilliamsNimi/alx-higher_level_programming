#!/usr/bin/python3
""" This is the rectangle test module """
import unittest
rectangle = __import__('models/rectangle').rectangle

class TestRectangle(unittest.TestCase):
    """ This is the test class for the rectangle class """
    

    def test___init__(self):
        """ This is the test function for init"""
        rect = rectangle(1, 2)
        self.assertEqual(rect.__width, 1)
        self.assertEqual(rect.__height, 2)
        rect2 = rectangle(1, 2, 3)
        self.assertEqual(rect2.__width, 1)
        self.assertEqual(rect2.__height, 2)
        self.assertEqual(rect2.__x, 3)

    def test_width(self):
        """ this is the test function of the width function """
        rect = rectangle(1, 2)
        self.assertEqual(rect.width(), 1)

    def test_height(self):
        """ this is the test function of the height function """
        rect = rectangle(1, 2)
        self.assertEqual(rect.height(), 2)

    def test_x(self):
        """ this is the test function of the x function """
        rect = rectangle(1, 2)
        self.assertEqual(rect.x(), 0)

    def test_y(self):
        """ this is the test function of the y function """
        rect = rectangle(1, 2)
        self.assertEqual(rect.y(), 0)

    def test_area(self):
        """ This is the test function of the area function """
        rect = rectangle(1, 2)
        self.assertEqual(rect.area(), 2)

if __name__ == '__main__':
    unittest.main()
