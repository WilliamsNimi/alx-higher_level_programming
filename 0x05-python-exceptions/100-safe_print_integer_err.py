#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return False
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
