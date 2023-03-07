#!/usr/bin/python3
start = 97
starter = 0
while start < 123:
    if start == 101:
        starter = starter + 1
    elif start == 113:
        starter = starter + 1
    else:
        print(f"{s}".format(chr(start)), end="")
    start = start + 1
