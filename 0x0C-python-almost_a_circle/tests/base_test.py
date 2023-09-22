#!/usr/bin/python3
""" This is a test module """
import unittest
base = __import__('models/base').base

class TestBase(unittest.TestCase):
    """ This is the base Test class """

    def test_to_json_string(self):
        """ This is the test function for to_json_string function"""
        self.assertEqual(type(base.to_json_string(self.__dict__)), dict)
        self.assertEqual(type(base.to_json_string([]), list))
        self.assertEqual(base.to_json_string([ { 'id': 12 }]), [{"id": 12}])
    
    def test_from_json_string(self):
        """This is the test function for the from_json_string"""
        self.assertEqual(type(base.from_json_string(None)), list)
        self.assertEqual(type(base.from_json_string("[]")), list)
        self.assertEqual(base.from_json_string('[{ "id": 89 }]'), [{"id":89}])

    def test___init__(self):
        """This function tests the Base constructor"""
        self.assertEqual(base.id, None)
        self.assertEqual(base.__nb_objects, 1)

if __name__ == '__main__':
    unittest.main()
