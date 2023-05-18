#!/usr/bin/env python3
"""
Concurrent Coroutines
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays
    """
    list_delays: List[float] = []
    for i in range(n):
        list_delays.append(await wait_random(max_delay))
    return sorted(list_delays)
