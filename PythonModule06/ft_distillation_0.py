#!/usr/bin/env python3


from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strenght_position: {strength_potion()}")
    print(f"Testing healing_position: {healing_potion()}")


if __name__ == "__main__":
    main()
