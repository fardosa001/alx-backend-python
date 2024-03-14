#!/usr/bin/env python3
""" type-annotated function returns sum of a list of float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of a list of floats"""
    return sum(input_list)
