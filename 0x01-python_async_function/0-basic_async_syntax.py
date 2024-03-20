#!/usr/bin/env python3
""" an asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ an asynchronous coroutine that takes an integer,
    waits for random delay between 0 and max_delay
    (included and float value) seconds and
    eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
