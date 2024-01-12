#!/usr/bin/python3
"""
Function that returns pascars triangle list of lists
"""


def pascal_triangle(n):
    """
    Function that returns pascals triangle as list

    Args:
        n (int): The length

    Returns:
        list: pascals triangle combination
    """
    if n <= 0:
        return []
    pascals = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = pascals[i - 1][j - 1] + pascals[i - 1][j]
            row.append(element)
        row.append(1)
        pascals.append(row)
    return pascals
