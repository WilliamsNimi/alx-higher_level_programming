#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for list_el in matrix:
        for nums in list_el:
            print("{:d}".format(nums), end=" ")
        print("")
