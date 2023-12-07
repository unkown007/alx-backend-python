#!/usr/bin/env python3
""" Define to_kv """
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """ Create a tuple composed of the arguments """
    return (k, v)
