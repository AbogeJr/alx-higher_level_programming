#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    items = len(my_list)
    if idx >= items or idx < 0:
        return my_list
    else:
        for i in range(items):
            if i == idx:
                del(my_list[i])

        return my_list
