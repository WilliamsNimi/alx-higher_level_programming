#!/usr/bin/python3


def weight_average(my_list=[]):
    num = 0
    den = 0
    if my_list:
        for tups in my_list:
            num = num + (tups[0] * tups[1])
            den = den + tups[1]
        return num / den
    else:
        return 0
