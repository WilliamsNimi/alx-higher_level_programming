#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    lists = sorted(list(a_dictionary.keys()))
    for items in lists:
        print("{}: {}".format(items, a_dictionary[items]))
