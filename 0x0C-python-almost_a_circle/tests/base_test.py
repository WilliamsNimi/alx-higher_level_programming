#!/usr/bin/python3
""" This is a test module """
import unittest
base = __import__('models/base').base

class TestBase(unittest.TestCase):
    """ This is the base Test class """

    def tests_to_json_string(self):
        """ This is the test function for to_json_string function"""
        pass

    def tests_save_to_file(self):
        """ This is the test function for save_to_file function """
        pass

if __name__ == '__main__':
    unittest.main()
