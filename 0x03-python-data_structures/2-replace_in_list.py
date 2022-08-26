#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    items = len(my_list)
    if idx >= items or idx < 0:
        return None
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list
