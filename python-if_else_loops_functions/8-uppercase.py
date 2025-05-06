#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) > 96):
            str = str[:i] + chr(ord(str[i]) - 32) + str[i + 1:]
    print(str)

uppercase("String")