#!/usr/bin/env python3

"""Complex types - string and int/float to tuple"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """type-annotated function that takes a string and an int OR float
    as arguments and returns a tuple. The first element of the tuple is
    the string.
    The second element is the square of the int/float
    and should be annotated as a float."""

    return (k, v**2)
