#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    full_list = []
    for i in matrix:
        lists = []
        for j in i:
            lists.append(j * j)
        full_list.append(lists)
    return full_list
