#!/usr/bin/env python3

"""Complex types - functions"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Write a type-annotated function
    that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""
    return floatmult(multiplier)


def floatmult(n: float):
    """function that multiplies a float"""
    return lambda x: x * n
