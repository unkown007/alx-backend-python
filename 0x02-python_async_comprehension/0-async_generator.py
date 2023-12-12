#!/usr/bin/env python3
""" Define async_generator """
from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """ Generate random integers """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
