#!/usr/bin/env python3
"""
Type-annotated function element_length that takes a list
input_list of strings and returns a list containing the
lengths of each string element
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list containing the lengths of each string element
    """
    return [(i, len(i)) for i in lst]
