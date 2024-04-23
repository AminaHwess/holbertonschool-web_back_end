#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """an asynchronous coroutine that takes in an integer argument
    that waits for a random delay eventually returns it."""
    waittime = random.uniform(0, max_delay)
    await asyncio.sleep(waittime)
    return waittime
