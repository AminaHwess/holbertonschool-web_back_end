#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """an async routine that takes in 2 int arguments.
        You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays.
    The list of the delays should be in ascending order."""
    delaylist = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delaylist.append(delay)
    return sorted(delaylist)
