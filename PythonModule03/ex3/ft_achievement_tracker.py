#!/usr/bin/env python3


import random


def gen_player_achievements(achievements: list) -> set:
    return set(random.sample(achievements, random.randint(3, 6)))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner",
                    "Survivor", "Treasure Hunter", "First Steps",
                    "Sharp Mind"]

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()

    achievements_set = set(achievements)
    print(f"All distinct achievements: {achievements_set}")

    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")

    print()
    print(f"Alice is missing: {achievements_set.difference(alice)}")
    print(f"Bob is missing: {achievements_set.difference(bob)}")
    print(f"Charlie is missing: {achievements_set.difference(charlie)}")
    print(f"Dylan is missing: {achievements_set.difference(dylan)}")


if __name__ == "__main__":
    main()
