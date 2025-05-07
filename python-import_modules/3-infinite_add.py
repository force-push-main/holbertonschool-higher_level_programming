#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    result = 0

    for num in argv:
        result += int(num)
    
    print(result)


if __name__ == "__main__":
    main()
