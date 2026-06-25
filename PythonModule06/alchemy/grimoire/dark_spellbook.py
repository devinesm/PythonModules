#!/usr/bin/env python3

from . import dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return (f"Spell recorded: {spell_name}"
            f"({dark_validator.validate_ingredients(ingredients)})")
