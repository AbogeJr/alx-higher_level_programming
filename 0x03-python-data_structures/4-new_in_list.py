#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    items = len(my_list)
    if idx >= items or idx < 0:
        return None
    else:
        new_list = my_list[:idx] + [element] + my_list[idx+1:]
        return new_list
