#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for list_el in matrix:
        i = 0
        for nums in list_el:
            if i < (len(list_el) - 1):
                print("{:d}".format(nums), end=" ")
            else:
                print("{:d}".format(nums), end="")
            i += 1
        print("")
