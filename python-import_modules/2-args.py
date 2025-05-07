#!/usr/bin/python3

def main(*argv):
    num_args = len(argv)
    if num_args == 0:
        print("{} arguments.".format(num_args))
        return
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:")
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))