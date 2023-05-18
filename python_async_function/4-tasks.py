#!/usr/bin/env python3
"""Tasks 4"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all the delays"""
    list_delays: List[float] = []
    for i in range(n):
        list_delays.append(await task_wait_random(max_delay))
    return sorted(list_delays)
