#!/usr/bin/env python3
""" Define the safe_first_element """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Gets the fist element of the list or Nothing """
    if lst:
        return lst[0]
    else:
        return None
