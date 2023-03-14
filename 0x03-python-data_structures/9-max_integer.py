#!/usr/bin/python3


def max_integer(my_list=[]):
    maxi = 0
    if len(my_list) == 0:
        return None
    else:
        maxi = my_list[0]
    for item in my_list:
        if item > maxi:
            maxi = item
    return maxi
