#!/usr/bin/env python3


from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast
from .strategy import BattleStrategy


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._creature_name}'"
                " for this aggressive strategy")
        transformation = cast(TransformCapability, creature)
        return [transformation.transform(),
                creature.attack(),
                transformation.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._creature_name}'"
                " for this defensive strategy")
        healing = cast(HealCapability, creature)
        return [creature.attack(), healing.heal("small")]
