#!/usr/bin/env python3

"""
executes multiple coroutines at once
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    wait_n: run concurrent tasks
    Args:
        n: int
        max_delay: int
    return: list
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = []
    for future in asyncio.as_completed(tasks):
        res = await future
        completed.append(res)

    return completed
