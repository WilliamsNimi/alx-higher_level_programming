#!/usr/bin/python3
from calculator_1.py import sub
from calculator_1.py import add
from calculator_1.py import mul
from calculator_1.py import div
def calculate():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    calculate()
