#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
