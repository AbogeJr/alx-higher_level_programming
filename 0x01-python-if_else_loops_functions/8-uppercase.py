#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = i
        if ord(i) in range(97, 123):
            char = chr(ord(i) - 32)
        print('{}'.format(char), end='')
    print()
