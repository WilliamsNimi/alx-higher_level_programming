#!/usr/bin.python3
""" This is the tes module for square """
import unittest
square = __import__('models/square.py').square

class TestSquare(unittest.TestCase):
    """ This is the Test class for the Square Class """

    def test_size(self):
        """ this is the test function for the size function """
        pass

    def test_update(self):
        """ This is the test function for the update function """
        pass

    def test_todictionary(self):
        """ This is the test function for the to_dictionary function """
        pass


if __name__ == '__main__':
    unittest.main()
