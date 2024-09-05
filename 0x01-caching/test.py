#!/usr/bin/env python3

MAX_ITEMS = 4


def dict_insert(new_dict, key, value):
    new_dict[key] = value
    if len(new_dict) > MAX_ITEMS:
        keys = list(new_dict.keys())
        last_key = keys[-2]
        # first_key = next(iter(new_dict))
        new_dict.pop(last_key)
        print(f"DISCARD: {last_key}\n")


def dict_delete(new_dict, key):
    new_dict.pop(key)


new_dict = {}
dict_insert(new_dict, "A", "Hello")
dict_insert(new_dict, "B", "World")
dict_insert(new_dict, "C", "Holberton")
dict_insert(new_dict, "D", "School")
dict_insert(new_dict, "E", "Python")
dict_insert(new_dict, "F", "is")
print(new_dict)
