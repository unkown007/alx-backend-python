#!/usr/bin/env python3
""" Define measure_time """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the execution time
    Args:
        n(int): times of execution
        max_delay(int): max_delay
    Return: time elapsed
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
