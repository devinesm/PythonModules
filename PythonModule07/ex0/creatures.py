#!/usr/bin/env python3

from .creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flaming", "Fire")

    def attack(self) -> str:
        return f"{self._creature_name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self._creature_name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self._creature_name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self._creature_name} uses Hydro Pump!"
