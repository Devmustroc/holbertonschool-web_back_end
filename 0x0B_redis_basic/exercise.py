#!/usr/bin/env python3
"""
Create a Cache Class that Store an instance of the Redis client
as a private variable named _redis and use the flushdb() method.
Create store method that takes a data argument and returns a string.
this method should generate a random key (e.g. using uuid),
"""
import functools
from typing import Union, Optional, Callable
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorator count calls"""
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        self._redis.incr(key)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator call history"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper


def replay(self, method: Callable) -> None:
    """Display the history of calls of a particular function."""
    local_redis = redis.Redis()
    pipe = local_redis.pipeline()

    key_input = method.__qualname__ + ":inputs"
    key_output = method.__qualname__ + ":outputs"

    history_input = local_redis.lrange(key_input, 0, -1)
    history_output = local_redis.lrange(key_output, 0, -1)

    results = list(zip(history_input, history_output))

    print(f"{method.__qualname__} was called {len(history_input)} times:")
    for i in results:
        print(f"{method.__qualname__}(*{i[0].decode()}) -> {i[1].decode()}")


class Cache:
    """Class Cache"""

    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Method get"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Method get_str"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Method get_int"""
        return self.get(key, int)
