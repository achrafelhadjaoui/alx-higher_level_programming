#!/usr/bin/python3

import json
import sys


load_function = __import__('6-load_from_json_file').load_from_json_file
save_function = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# load
try:
    my_list = load_function(filename)
except FileNotFoundError:
    my_list = []

# add
for i in sys.argv[1:]:
    my_list.append(i)

# save
save_function(my_list, filename)
