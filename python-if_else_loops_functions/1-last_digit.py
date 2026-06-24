#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if not isinstance(number, int):
    raise TypeError("number must be an integer")
number_str = str(number)
last_digit = int(number_str[-1])
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    comparison = "and is greater than 5"
elif last_digit == 0:
    comparison = "and is 0"
elif last_digit < 6 and last_digit != 0:
    comparison = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, comparison))
