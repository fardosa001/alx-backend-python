#!/usr/bin/env python3
"""a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task."""
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regular function returning an asyncio.Task"""
    return asyncio.ensure_future(wait_random(max_delay))
