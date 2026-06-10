#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 16:52:24 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/10 17:42:02 by ipinto-m          ###   ########.fr       #
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

    def grow(self, growth_value: float) -> None:
        self._height += growth_value

    def age_up(self, age_value: int) -> None:
        self._age += age_value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height:.0f}cm")
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


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("rose", 15.0, 10)

    print("Plant created: ", end="")
    plant.show()

    print()

    plant.set_height(25.0)
    plant.set_age(30)

    print()

    plant.set_height(-1)
    plant.set_age(-1)

    print()

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
