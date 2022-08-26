#!/usr/bin/python3
def element_at(my_list, idx):
    items = len(my_list)
    if idx >= items or idx < 0:
        return None
    else:
        return my_list[idx]
