#!/usr/bin/python3
""" This Script fethces url based on user provided argument"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.info()['X-Request-Id'])
