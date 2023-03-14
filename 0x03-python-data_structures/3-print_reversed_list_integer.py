#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        idx = -1
        for item in my_list:
            print("{:d}".format(my_list[idx]))
            idx -= 1
