#!/usr/bin/env python3

"""
complex types- funtions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: multier funtion
    Args:
        multiplier: multiplier
    return: funtion that multiplies
    """

    def multiplier_func(n: float) -> float:
        """
        return: n * multiplier
        Args:
            n: float
        """
        return n * multiplier
    return multiplier_func
