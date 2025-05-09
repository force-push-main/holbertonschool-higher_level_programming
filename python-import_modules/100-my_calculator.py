#!/usr/bin/python3
import calculator1
import sys


def main():
    argv = sys.argv[1:]
    calc_fncs = {
        "+": calculator1.add,
        "-": calculator1.sub,
        "*": calculator1.mul,
        "/": calculator1.div
    }

    if (len(argv) < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        if argv[1] in calc_fncs:
            result = calc_fncs[argv[1]](int(argv[0]), int(argv[2]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} + {} = {}".format(argv[0], argv[2], result))


if __name__ == "__main__":
    main()
