#!/usr/bin/python3


def my_func(matrix):
    full_list = []
    for i in matrix:
        lists = []
        for j in i:
            lists.append(j * j)
        full_list.append(lists)
    print(full_list)

def square_matrix_simple(matrix=[]):
    my_func(matrix)
