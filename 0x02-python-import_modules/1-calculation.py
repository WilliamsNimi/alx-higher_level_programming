#!/usr/bin/python3
from calculator_1.py import sub
from calculator_1.py import add
from calculator_1.py import mul
from calculator_1.py import div
def calculate():
    a = 10
    b = 5
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    print("{} + {} = {}".format(a, b, c))
    print("{} - {} = {}".format(a, b, d))
    print("{} * {} = {}".format(a, b, e))
    print("{} / {} = {}".format(a, b, f))

if __name__ == "__main__":
    calculate()
