#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, creature_name: str, creature_type: str) -> None:
        self._creature_name = creature_name
        self._creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        string = f"{self._creature_name} is a"
        string += f" {self._creature_type} type Creature"
        return string
