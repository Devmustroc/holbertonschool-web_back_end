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
    start: float = time.perf_counter()
    for _ in range(n):
        wait_n(max_delay)
    total_time: float = time.perf_counter() - start

    return total_time / n
