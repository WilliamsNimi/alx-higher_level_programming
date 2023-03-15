#!/usr/bin/python3
import hidden_4


def unhide():
    for values in dir(hidden_4):
        if values[0] != "_" and values[1] != "_":
            print(values)

if __name__ == "__main__":
    unhide()
