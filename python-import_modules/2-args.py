#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv) - 1
    while True:
        if num_arg == 1:
            print("1 argument: ")
            break
        elif num_arg == 0:
            print("0 arguments.")
            break
        else:
            print("{} arguments:".format(num_arg))
            for i in range(1, num_arg + 1):
                print("{}: {}".format(i, argv[i]))
                break
