#!/usr/bin/env python3
"""
runtime for 4 parallel opratios
"""

import asyncio
import time
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_time: meausre tasks runtime
    return: time elapsed
    """
    start = time.perf_counter()
    tasks = [async_c(), async_c(), async_c(), async_c()]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    return elapsed
