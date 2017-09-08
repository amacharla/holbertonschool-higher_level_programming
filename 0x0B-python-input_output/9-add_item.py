#!/usr/bin/python3

save = __import__('7-save_to_json_file').save_to_json_file
# def save_to_json_file(my_obj, filename)
load = __import__('8-load_from_json_file').load_from_json_file
# def load_from_json_file(filename)

from sys import argv
filename = "add_item.json"
current_args = argv[1:]
try:
    file_args = load(filename)
    current_args += file_args
except:
    save(current_args, filename)
    load(filename)
