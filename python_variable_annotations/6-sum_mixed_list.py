#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list which takes a list mxd_lst
of floats and integers and returns their sum as a float
"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns their sum as a float
    """
    return sum(mxd_list)
