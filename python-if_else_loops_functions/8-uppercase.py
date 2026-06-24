#!/usr/bin/python3
def uppercase(str):
    if ord(str) in range(97, 122):
        print("{}".format(char(ord(str)+32)))
    else:
        print("{}".format(str))
