#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Returns total_time / n
    """
    start_time: float = asyncio.get_event_loop().time()
    await wait_n(n, max_delay)
    end_time: float = asyncio.get_event_loop().time()
    total_time: float = end_time - start_time
    return total_time / n
