#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_intro.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/10 09:10:43 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/10 17:41:42 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro(name: str, height: int, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    print("=== Welcome to My Garden ===")

    name = "Rose"
    height = 25
    age = 30

    ft_garden_intro(name, height, age)
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
