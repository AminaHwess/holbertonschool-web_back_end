#!/usr/bin/env python3

"""Let's duck type an iterable object"""

import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Return a list of tuples containing the sequence
    and its length for each element in lst."""

    return [(i, len(i)) for i in lst]
