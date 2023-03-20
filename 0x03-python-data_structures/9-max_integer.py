#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    b = my_list[0]
    for x in range(len(my_list)):
        if b < mylist[x]:
            b = mylist[x]
    return b
