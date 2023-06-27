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

    def replay(self, method: Callable):
        """Method replay"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        input_history = self._redis.lrange(input_key, 0, -1)
        output_history = self._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(input_history)} times:")

        for input1, output1 in zip(input_history, output_history):
            print(f"{method.__qualname__}(*{input1.decode('utf-8')}) -> "
                  f"{output1.decode('utf-8')}")


