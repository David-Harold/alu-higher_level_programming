#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        ascii_code = ord(char)
        if ascii_code in range(97, 123):
            char = chr(ascii_code - 32)
        new_str += char

    print("{}".format(new_str))
