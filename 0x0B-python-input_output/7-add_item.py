#!/usr/bin/python3
import json
import sys
save_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" This is a load, add , save module """

i = 0
arg_list = []
for items in sys.argv:
    if i != 0:
        arg_list.append(items)
    i += 1
saved_json = save_json_file(arg_list, "add_item.json")
print(load_from_json_file("add_item.json"))
