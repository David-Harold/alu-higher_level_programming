#!/usr/bin/python3
def uppercase(str):
    if ord(str) in range(97, 122):
        print(char(ord(str)+32))
    else:
        print(str)
