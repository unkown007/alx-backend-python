#!/usr/bin/env python3
""" Define sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum all the elements of the list
    Args:
        input_list(list[int]): list of floats
    Return: sum of all elements
    """
    return float(sum(input_list))
