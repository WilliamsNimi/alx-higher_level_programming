#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    count = 0
    if idx < 0 or  idx >= len(my_list):
        return my_list
    for item in my_list:
        if count == idx:
            my_list.remove(item)
        count += 1
    return my_list
