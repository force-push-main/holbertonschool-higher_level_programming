#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print("{} arguments.".format(num_args))
        return
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
