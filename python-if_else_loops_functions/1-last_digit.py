#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(number_str[-1])
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    comparison = "and is greater than 5\n"
elif last_digit == 0:
    comparison = "and is 0\n"
elif last_digit < 6 and last_digit != 0:
    comparison = "and is less than 6 and not 0\n"
print("Last digit of {} is {} {}".format(number,last_digit,comparison))
