#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len > 1 and b_len > 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if a_len == 0:
        return tuple_b
    elif b_len == 0:
        return tuple_a
    elif a_len == 1 and b_len == 1:
        return (tuple_a[0] + tuple_b[0], 0)
    elif a_len == 1:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif b_len == 1:
        return (tuple_a[0] + tuple_b[0], tuple_a[1])
