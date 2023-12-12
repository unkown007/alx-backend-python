#!/usr/bin/env python3
""" Define measure_runtime """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime of async comprehension """
    start_time = time.time()
    await asyncio.gather(
        *tuple(map(lambda _: async_comprehension(), range(4)))
    )
    return time.time() - start_time
