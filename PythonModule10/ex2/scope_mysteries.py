#!/usr/bin/env python3

from typing import Callable, Any
import data_generator


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    print("🌊 Memory Depths Testing with Data Generator 🌊")
    print("==================================================")

    gen = data_generator.FuncMageDataGenerator

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    powers = gen.generate_spell_powers(3)
    base_power = powers[0]
    add1, add2 = powers[1], powers[2]

    acc = spell_accumulator(base_power)
    print(f"Base {base_power}, add {add1}: {acc(add1)}")
    print(f"Base {base_power}, add {add2}: {acc(add2)}")

    print("\nTesting enchantment factory...")
    enchant1 = enchantment_factory(gen.ENCHANTMENT_TYPES[0])
    enchant2 = enchantment_factory(gen.ENCHANTMENT_TYPES[1])

    items = gen.generate_enchantment_items(2)
    print(enchant1(items[0]))
    print(enchant2(items[1]))

    print("\nTesting memory vault...")
    vault_funcs = memory_vault()
    store_memory = vault_funcs['store']
    recall_memory = vault_funcs['recall']

    secret_spell = gen.generate_spells(1)[0]

    print(f"Store 'secret_spell' = {secret_spell}")
    store_memory('secret_spell', secret_spell)

    print(f"Recall 'secret_spell': {recall_memory('secret_spell')}")
    print(f"Recall 'unknown_key': {recall_memory('unknown_key')}")


if __name__ == "__main__":
    main()
