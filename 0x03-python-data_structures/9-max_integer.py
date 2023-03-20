#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    b = my_list[0]
    for x in my_list:
        if x > b:
            b = x
    return b
