#!/usr/bin/env python3
""" Define to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Create a tuple composed of the arguments """
    return (k, float(v ** 2))
