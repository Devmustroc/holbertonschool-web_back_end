#!/usr/bin/env python3
"""
Create a Cache Class that Store an instance of the Redis client
as a private variable named _redis and use the flushdb() method.
Create store method that takes a data argument and returns a string.
this method should generate a random key (e.g. using uuid),
"""
from typing import Union

import redis
import uuid


class Cache:
    """Class Cache"""
    def __init__(self) -> None:
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
