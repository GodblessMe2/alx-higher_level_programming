#!/usr/bin/python3
"""Contains the "pascal_triangle" function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
        Returns a list of lists of integers representing the triangle.
    """
    listItem = [[1]]

    if n <= 0:
        return []

    while len(listItem) != n:
        triangle = listItem[-1]
        tmp = [1]
        for i in range(len(triangle)-1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        listItem.append(tmp)
    return listItem
