#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_t = 0
    for i in argv[1:]:
        sum_t += int(i)
    print(sum_t)
