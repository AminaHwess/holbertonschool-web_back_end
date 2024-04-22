#!/usr/bin/env python3

"""Complex types - mixed list"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """type-annotated function which takes a list
    of integers and floats and returns their sum as a float."""
    sum = float(0)
    for nbr in mxd_lst:
        sum += float(nbr)
    return sum
