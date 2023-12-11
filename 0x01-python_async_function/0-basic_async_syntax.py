#!/usr/bin/env python3
"""
a basic random function with asyncio
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: generate radom float
    Args:
        max_delay: int
    return: float
    """
    rn = uniform(0, max_delay)
    await asyncio.sleep(rn)
    return rn
