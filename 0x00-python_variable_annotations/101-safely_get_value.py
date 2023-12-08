#!/usr/bin/env python3
""" Define safe_get_value """
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ Get the value of a dict or return default value if not found """
    if key in dct:
        return dct[key]
    else:
        return default
