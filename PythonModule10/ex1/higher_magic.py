#!/usr/bin/env python3

from typing import Callable
import data_generator


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(target: str, power: int) -> str | Callable[[str, int], str]:
        if (condition(target, power)):
            return spell(target, power)
        return ("Spell fizzled")
    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        sequence = []
        for spell in spells:
            sequence.append(spell(target, power))
        return sequence
    return sequence


def main() -> None:
    print("✨ Higher Realm Testing with Data Generator ✨")
    print("==================================================")

    gen = data_generator.FuncMageDataGenerator

    generated_powers = gen.generate_spell_powers(3)
    p1, p2, p3 = generated_powers[0], generated_powers[1], generated_powers[2]

    targets = ["Dragon", "Goblin", "Wizard", "Knight"]
    target = targets[2]

    print(f"Target: {target}")
    print(f"Generated Powers: {generated_powers}")
    print("-" * 50)

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    combo_results = combined_spell(target, p1)
    print(f"Combined spell result: {combo_results[0]}, {combo_results[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {p2}, Amplified: {p2 * 3}")
    print(mega_fireball(target, p2))

    print("\nTesting conditional caster (Requires Power >= 25)...")

    def power_condition(t: str, p: int) -> bool:
        return p >= 25

    fussy_spell = conditional_caster(power_condition, fireball)

    print(f"Power {p1} cast:", fussy_spell(target, p1))
    print(f"Power {p3} cast:", fussy_spell(target, p3))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    results = sequence(target, p2)
    for res in results:
        print(f" -> {res}")


if __name__ == "__main__":
    main()
