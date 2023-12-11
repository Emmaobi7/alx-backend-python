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
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    res = await asyncio.gather(*tasks)
    return sorted(res)
