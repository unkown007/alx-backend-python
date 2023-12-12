#!/usr/bin/env python3
""" Define async_generator """
from typing import AsyncGenerator
from random import uniform
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """ Generate random integers """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
