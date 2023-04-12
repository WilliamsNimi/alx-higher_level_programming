#!/usr/bin/python3

""" This is the file reader function """


def read_file(filename=""):
    """ This is the readfile function """
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end='')
