#!/usr/bin/python3


def search_replace(my_list, search, replace):
    lists = []
    lists2 = my_list.copy()
    for values in range(0, len(my_list)):
        if lists2[values] == search:
            lists2[values] = replace
        lists.append(lists2[values])
    return lists
