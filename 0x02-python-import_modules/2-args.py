#!/usr/bin/python3
import sys


def cmdargs():
    count = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print("{} argument:"
                  .format((len(sys.argv) - 1)))
            print("{}: {}".format(count, sys.argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv)-1))
            for i in range(len(sys.argv)-1):
                print("{}: {}".format((count), sys.argv[count]))
                count += 1


if __name__ == "__main__":
    cmdargs()
