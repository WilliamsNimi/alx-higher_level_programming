#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        return "00"
    if number < 0:
        mod = ((number * -1) % 10) * -11
    else:
        mod = number % 10
    return mod
