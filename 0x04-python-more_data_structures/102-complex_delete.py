#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values_list = list(a_dictionary.values())
    keys_list = list(a_dictionary.keys())
    if value in values_list:
        a_dictionary.pop(keys_list[values_list.index(value)])
    return a_dictionary
