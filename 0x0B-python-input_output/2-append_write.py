#!/usr/bin/python3
""" This is an append function """


def append_write(filename="", text=""):
    """ This is an append file function """
    with open(filename, mode='a', encoding="UTF8") as file:
        return file.write(text)
