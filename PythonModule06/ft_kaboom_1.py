#!/usr/bin/env python3


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print("Testing record dark spell:"
              f" {dark_spell_record('Curse', 'bats, frogs')}")
    except ImportError as e:
        print(e)


if __name__ == "__main__":
    main()
