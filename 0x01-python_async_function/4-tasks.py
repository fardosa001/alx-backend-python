#!/usr/bin/env python3
"""task_wait_n function"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values) in ascending order
    without using sort() because of concurrency"""
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        insert_index = 0
        while insert_index < len(delays) and delay > delays[insert_index]:
            insert_index += 1
        delays.insert(insert_index, delay)
    return delays
