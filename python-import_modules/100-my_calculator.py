#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

def main():
    args = argv[1:]
    calc_fncs = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if (len(args) < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] in calc_fncs:
        result = calc_fncs[args[1]](int(args[0]), int(args[2]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} + {} = {}".format(args[0], args[2], result))


if __name__ == "__main__":
    main()
