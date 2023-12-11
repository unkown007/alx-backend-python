#!/usr/bin/env python3
""" Define task_wait_random """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Create and asyncio Task and return it """
    return asyncio.create_task(wait_random(max_delay))
