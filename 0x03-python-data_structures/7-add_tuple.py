#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if a == 0 and b:
        return tuple_b
    elif b == 0 and a:
        return tuple_a
    elif a == 1 and b >= 2:
        return (tuple_a[0]+tuple_b[0], tuple_b[1])
    elif b == 1 and a >= 2:
        return (tuple_a[0]+tuple_b[0], tuple_a[1])
    else:
        return (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
