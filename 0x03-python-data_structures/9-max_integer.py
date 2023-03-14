#!/usr/bin/python3


def max_integer(my_list=[]):
    maxi = 0
    if len(my_list) == 0:
        return None
    for item in my_list:
        if item < 0:
            maxi = item
        if item > maxi:
            maxi = item
    return maxi
