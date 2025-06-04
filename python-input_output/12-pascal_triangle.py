#!/usr/bin/python3
"""function that prints pascal's triangle"""


def pascal_triangle(n):
    """pascal_triangle function"""

    triangle = []

    for i in range(n):
        sublist = []
        for k in range(i + 1):
            if k == 0 or k == i:
                sublist.append(1)
            else:
                el = triangle[i - 1][k] + triangle[i - 1][k - 1]
                sublist.append(el)
        triangle.append(sublist)

    return triangle
