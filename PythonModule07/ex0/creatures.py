from .creature import Creature

class Flameling(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack() -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack() -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack() -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack() -> str:
        return "Torragon uses Hydro Pump!"