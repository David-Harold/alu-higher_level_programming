#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = []
    f1 = my_list[0]
    temp.append(f1)
    for i in my_list:
        if i > temp[0]:
            temp[0] = i
    return temp[0]
