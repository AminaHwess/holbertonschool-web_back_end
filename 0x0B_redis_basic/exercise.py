#!/usr/bin/env python3
import redis
import uuid
from functools import wraps
from typing import Union, Callable

"""
 Cache Class
 """


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment count and call original method."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store input/output history and call original."""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    """Cache class to store data in redis db"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method generate random key and
        store data in it in the redis db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float, None]:
        """will return converted data back to the desired format"""
        data = self._redis.get(key)
        if data is None:
            return None
        else:
            if fn is None:
                return data
            else:
                return fn(data)

    def get_str(self, key: str) -> str:
        """will automatically parametrize Cache.get"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """will automatically parametrize Cache.get"""
        return self.get(key, fn=int)
