#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine that loops 10 times asynchronously wait 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
