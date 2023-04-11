#!/usr/bin/python3


""" This module is a child of the List class """
class MyList(list):
    """ This is the MyList class """

    def print_sorted(self):
        """ This is the print sorted list function """
        newList = self[:]
        newList.sort()
        print(newList)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
