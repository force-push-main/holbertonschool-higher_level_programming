#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    argv = sys.argv[1:]
    calc_fncs = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if (len(argv) < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        if argv[1] in calc_fncs:
            print(calc_fncs[argv[1]](int(argv[0]), int(argv[2])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
