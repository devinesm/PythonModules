#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    valid = light_spell_allowed_ingredients()
    if any(item.lower() in ingredients.lower() for item in valid):
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
