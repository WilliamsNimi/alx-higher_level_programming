#!/usr/bin/python3
""" This Script fethces url"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        r_read = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(r_read)))
        print('\t- content: {}'.format(r_read))
        print('\t- utf8 content: {}'.format(r.__dict__['msg']))
