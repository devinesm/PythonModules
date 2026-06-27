from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name = name
        self._creature_type = type

    @abstractmethod
    def attack() -> str:
        pass

    def describe(name: str, creature_type: str) -> str:
        return f"{name} is a {creature_type} Creature"