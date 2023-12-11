#!/usr/bin/env python3
""" Define wait_n """
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with the specified max_delay
    Args:
        n(int): number of time to spawn
        max_delay(int): maximum delay
    Return: list of floats of spawn numbers
    """
    spawn_number: list = []
    for _ in range(n):
        spawn_number.append(await wait_random(max_delay))
    return sorted(spawn_number)
