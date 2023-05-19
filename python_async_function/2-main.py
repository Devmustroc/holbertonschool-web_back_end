import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Returns total_time / n
    """
    start_time: float = asyncio.get_event_loop().time()
    await asyncio.run(wait_n(n, max_delay))
    end_time: float = asyncio.get_event_loop().time()
    total_time: float = end_time - start_time
    return total_time / n

async def main():
    n = 10
    max_delay = 1000
    print(await measure_time(n, max_delay))

if __name__ == "__main__":
    asyncio.run(main())