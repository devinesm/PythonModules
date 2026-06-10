#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 16:52:14 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/10 17:14:49 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self, growth_value: float) -> None:
        self.height += growth_value

    def age_up(self, age_value: int) -> None:
        self.age += age_value


def main() -> None:
    rose = Plant("rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(0.8)
        rose.age_up(1)
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
