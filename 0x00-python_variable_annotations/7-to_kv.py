#!/usr/bin/env python3

"""
sting and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: to tuple
    Args:
        K: string
        v: int or foat
    return: string and float tuple
    """
    return k, v**2
