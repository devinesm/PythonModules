#!/usr/bin/env python3

from functools import reduce, lru_cache, partial, singledispatch
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
    return {
        'fire': partial(base_enchantment, power=50, element='Fire'),
        'ice': partial(base_enchantment, power=50, element='Ice'),
        'lightning': partial(base_enchantment, power=50, element='Lightning')
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n needs to be positive")
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(arg: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast {len(arg)} spells"

    return cast


def main() -> None:
    print("📚 Ancient Library Testing 📚")
    print("========================================")

    print("\n--- Testing: spell_reducer ---")
    powers = [10, 20, 30]
    print(f"Base powers: {powers}")
    print(f"Addition: {spell_reducer(powers, 'add')}")
    print(f"Multiplication: {spell_reducer(powers, 'multiply')}")
    print(f"Maximum: {spell_reducer(powers, 'max')}")

    print("\n--- Testing: partial_enchanter ---")

    def base_spell(target: str, power: int, element: str) -> str:
        return f"{element} hits {target} with {power} power!"

    grimoire = partial_enchanter(base_spell)
    fire_strike = grimoire["fire"]
    ice_strike = grimoire["ice"]

    print(fire_strike("Goblin"))
    print(ice_strike("Dragon"))

    print("\n--- Testing: memoized_fibonacci ---")
    print(f"Fibonacci(10): {memoized_fibonacci(10)}")
    print(f"Fibonacci(35): {memoized_fibonacci(35)}")

    print("\n--- Testing: spell_dispatcher ---")
    caster = spell_dispatcher()
    print(caster(150))
    print(caster("Invisibility"))
    print(caster(["fireball", "heal"]))
    print(caster(3.14))


if __name__ == "__main__":
    main()
