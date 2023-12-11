#!/usr/bin/env python3
""" Define wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay
    Args:
        max_delay(float): max delay the function can make
    Return: max delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
