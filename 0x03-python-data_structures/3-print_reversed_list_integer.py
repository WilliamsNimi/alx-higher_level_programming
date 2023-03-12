#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        pass
    idx = -1
    for item in my_list:
        print("{:d}".format(my_list[idx]))
        idx -= 1
