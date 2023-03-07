#!/usr/bin/python3
def uppercase(str):
    cha = 0
    str2 = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <=123:
            cha = ord(ch) - 32
            str2 = str2 + chr(cha)
        else:
            str2 = str2 + ch
    print("{s}".format(str2))
