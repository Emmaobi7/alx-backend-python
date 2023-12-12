#!/usr/bin/env python3
"""
asynchronous comprehension
list
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_genrator: async_gen 10x
    return: list
    """
    res = [data async for data in async_generator()]
    return res
