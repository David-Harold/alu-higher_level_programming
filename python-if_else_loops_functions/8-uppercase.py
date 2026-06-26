#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print("{}".format(result))
