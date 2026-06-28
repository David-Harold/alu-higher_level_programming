#!/usr/bin/python3
import sys
from calculator_1
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if operator == "+":
        print(calculator_1.add(a, b))
    elif operator == "-":
        print(calculator_1.sub(a, b))
    elif operator == "*":
        print(calculator_1.mul(a, b))
    elif operator == "/":
        if b == 0:
            print("Can't divide by zero!")
            sys.exit(1)
        print(calculator_1.div(a, b))
