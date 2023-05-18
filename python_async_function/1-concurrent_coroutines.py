#!/usr/bin/env python3
"""
Concurrent Coroutines
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay seconds.

  Args:
    max_delay: The maximum delay in seconds.

  Returns:
    The delay in seconds.
  """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n, max_delay):
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

