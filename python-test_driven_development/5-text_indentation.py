#!/usr/bin/python3
"""function prints text with indents"""


def text_indentation(text):
    """function reformats text based on spec chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spec_chars = ['.', '?', ':']
    printed_newline = False
    for c in text:
        if printed_newline and (c == ' ' or c == '  '):
            printed_newline = False
            continue
        else:
            printed_newline = False
        if c in spec_chars:
            print(f"{c}\n")
            printed_newline = True
        else:
            print(c, end="")
