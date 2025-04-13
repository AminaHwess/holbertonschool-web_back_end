#!/usr/bin/env python3
"""
This module contains the Cache class and helper functions.
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable


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
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    r = redis.Redis()
    method_name = method.__qualname__
    input_key = method_name + ":inputs"
    output_key = method_name + ":outputs"

    count = r.get(method_name)
    if count is None:
        print(f'{method_name} was not called')
        return

    count = int(count)
    print(f'{method_name} was called {count} times:')

    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)

    for inp, out in zip(inputs, outputs):
        print(f'{method_name}{inp.decode("utf-8")} -> {out.decode("utf-8")}')


class Cache:
    """Cache class to store data in redis db"""

    def __init__(self):
        """initialise redis client and flush db"""
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
        """Retrieves data from redis, applying a conversion function if given.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieves a string from redis."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves an integer from redis."""
        return self.get(key, int)
