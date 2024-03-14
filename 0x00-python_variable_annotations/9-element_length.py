#!/usr/bin/env python3
"""Annotation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples."""
    return [(i, len(i)) for i in lst]
