#!/usr/bin/env python3

"""Run time for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """A coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it."""
    coros = [async_comprehension() for i in range(4)]
    start_time = time.time()
    await asyncio.gather(*coros)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
