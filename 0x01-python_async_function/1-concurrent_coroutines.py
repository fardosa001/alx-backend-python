#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values) in ascending order
    without using sort() because of concurrency"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        insert_index = 0
        while insert_index < len(delays) and delay > delays[insert_index]:
            insert_index += 1
        delays.insert(insert_index, delay)
    return delays
