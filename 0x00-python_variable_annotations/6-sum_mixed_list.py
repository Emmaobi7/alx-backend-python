#!/usr/bin/env python3

"""
Complex types (mixed list)
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: sum of mixed list
    Args:
       mxd_list: mixed list
    return: float
    """
    return sum(mxd_list)
