#!/usr/bin/python3
for i in range(10):
    for o in range(i+1, 10):
        if i == 8 and o == 9:
            print("{0}{1}".format(i, o))
        else:
            print("{0}{1}, ".format(i, o), end="")
