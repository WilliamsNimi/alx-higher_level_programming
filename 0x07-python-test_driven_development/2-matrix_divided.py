#!/usr/bin/python3


def matrix_divided(matrix, div):
    """ this is a scalar matrix division function """
    rowCount = len(matrix[0])
    rowCount2 = 0
    fullList = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for items in matrix:
        innerList = []
        rowCount2 = len(items)
        if rowCount2 != rowCount:
            raise TypeError("Each row of the matrix must have the same size")
        for nums in items:
            if type(nums) == int or type(nums) == float:
                innerList.append(round((nums / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        fullList.append(innerList)
    return fullList
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt", optionflags=doctest.ELLIPSIS)
