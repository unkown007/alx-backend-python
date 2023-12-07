#!/usr/bin/env python3
""" Define make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multipies a float by multiplier """
    def fun(x: float) -> float:
        return multiplier * x
    return fun
