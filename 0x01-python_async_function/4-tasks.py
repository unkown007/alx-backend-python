#!/usr/bin/env python3
""" Define task_wait_n """
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with the specified max_delay
    Args:
        n(int): number of time to spawn
        max_delay(int): maximum delay
    Return: list of floats of spawn numbers
    """
    spawn_number = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(spawn_number)
