#!/usr/bin/env python3
"""
Concurrent Coroutines
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Waits for a random delay between 0 and max_delay seconds n times.

      Args:
        n: The number of times to wait.
        max_delay: The maximum delay in seconds.

      Returns:
        A list of the delays in seconds.
      """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    delays.sort()
    return delays
