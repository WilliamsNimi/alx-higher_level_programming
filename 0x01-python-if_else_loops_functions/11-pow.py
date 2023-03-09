#!/usr/bin/python3
def pow(a, b):
    power = a
    if b < 0:
        for i in range((b*-1)+2):
            power = power / power
        return power
    for i in range(b-1):
        power = power * a
    return power
