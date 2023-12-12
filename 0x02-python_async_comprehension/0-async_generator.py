#!/usr/bin/env python3
"""
async generator for random numbers
10 x
"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator: generates random n
    return: generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
