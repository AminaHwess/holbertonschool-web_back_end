#!/usr/bin/env python3

"""Complex types - list of floats"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """type-annotated function which takes a list of floats as argument
    and returns their sum as a float."""
    sum = float(0)
    for nbr in input_list:
        sum += nbr
    return sum
