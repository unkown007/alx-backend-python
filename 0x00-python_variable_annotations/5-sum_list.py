#!/usr/bin/env python3
""" Define sum_list """


def sum_list(input_list: list[float]) -> float:
    """ Sum all the elements of the list
    Args:
        input_list(list[int]): list of floats
    Return: sum of all elements
    """
    total: float = 0.0
    for x in input_list:
        total += x
    return float(total)
