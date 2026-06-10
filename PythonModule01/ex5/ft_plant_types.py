#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_types.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 16:52:30 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/10 18:02:03 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, growth: float) -> None:
        self._height += growth

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height:.1f}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int) -> None:
        if days >= 0:
            self._age = days
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True

    def get_color(self) -> str:
        return self._color

    def get_bloom(self) -> bool:
        return self._bloom

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color()}")
        if self.get_bloom():
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade "
              f"of {self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_diameter():.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow_and_age(self, amount: int) -> None:
        for _ in range(amount):
            self._nutritional_value += 1
            super().grow(2.1)
            super().age()
        print(f"[make {self._name} grow and age for {amount} days]")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.get_harvest_season().capitalize()}")
        print(f"Nutritional value: {self.get_nutritional_value()}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()

    print()

    print("=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()

    print()

    print("=== Vegetable")
    vegetable = Vegetable("tomato", 5.0, 10, "april", 0)
    vegetable.show()
    vegetable.grow_and_age(20)
    vegetable.show()


if __name__ == "__main__":
    main()
