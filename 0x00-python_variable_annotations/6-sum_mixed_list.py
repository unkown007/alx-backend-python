#!/usr/bin/env python3
""" Define sum_mixed_list """
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """ Comput the sum of all elements of the list
    Args:
        mxd_lst(list): list of integer and floats
    Return: sum of all elements inside the list
    """
    return float(sum(mxd_lst))
