#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ai = 0
    b = 0
    ci = 0
    d = 0
    if len(tuple_a) == 1 and len(tuple_b) == 1:
        return ((tuple_a[0] + tuple_b[0]), 0)
    if len(tuple_a) == 1 and len(tuple_b) >= 2:
        ai = tuple_a[0]
        ci = tuple_b[0]
        d = tuple_b[1]
        return ((ai + ci), (b + d))
    if len(tuple_b) == 1 and len(tuple_a) >= 2:
        ci = tuple_b[0]
        ai = tuple_a[0]
        b = tuple_a[1]
        return ((ai + ci), (b + d))
    if len(tuple_a) == 0 and len(tuple_b) != 0:
        return tuple_b
    if len(tuple_b) == 0 and len(tuple_a) != 0:
        return tuple_a
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return (0, 0)
