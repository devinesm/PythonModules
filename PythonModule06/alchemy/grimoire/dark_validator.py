#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid = dark_spell_allowed_ingredients()
    for ingredient in valid:
        if (ingredient != ingredients.lower()):
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
