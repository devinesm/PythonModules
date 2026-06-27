#!/usr/bin/env python3


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        import alchemy.grimoire.dark_spellbook as da
        print("Testing record dark spell:"
              f" {da.dark_spell_record('Curse', 'bats, frogs')}")
    except ImportError as e:
        print(e)


if __name__ == "__main__":
    main()
