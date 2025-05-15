#!/usr/bin/python3
"""function prints text with indents"""


def text_indentation(text):
    """function reformats text based on spec chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spec_chars = ".?:"
    alpha_chars = "abcdefghijklmnopqrstuvwxyz"
    printed_newline = False
    for c in text:
        if printed_newline and c.lower() in alpha_chars:
            printed_newline = False
        elif printed_newline:
            continue
        if c in spec_chars:
            print(f"{c}\n")
            printed_newline = True
        else:
            print(c, end="")
