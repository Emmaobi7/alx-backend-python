#!/usr/bin/env python3

"""
i say duck typing only
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    checks element lenght
    """
    return [(i, len(i)) for i in lst]
