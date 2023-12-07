#!/usr/bin/env python3
"""
add type annotation to function
TypeVar
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    safely_get_vale: check dict
    add type annotation
    """
    if key in dct:
        return dct[key]
    else:
        return default
