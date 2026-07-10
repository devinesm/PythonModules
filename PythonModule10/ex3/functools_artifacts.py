#!/usr/bin/env python3

from functools import reduce, lru_cache
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n needs to be positive")
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    pass