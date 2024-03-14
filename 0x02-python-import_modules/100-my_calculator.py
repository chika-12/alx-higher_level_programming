#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """A working calculator"""
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1
    if count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    if opp != '+' and opp != '-' and opp != '*' and opp != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    elif opp == '+':
        print("{} {} {} = {}".format(a, opp, b, add(a, b)))
    elif opp == '-':
        print("{} {} {} = {}".format(a, opp, b, sub(a, b)))
    elif opp == '*':
        print("{} {} {} = {}".format(a, opp, b, mul(a, b)))
    elif opp == '/':
        print("{} {} {} = {}".format(a, opp, b, div(a, b)))
