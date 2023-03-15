#!/usr/bin/python3


def uniq_add(my_list=[]):
    lists = []
    for items in my_list:
        if items not in lists:
            lists.append(items)
    return sum(lists)
