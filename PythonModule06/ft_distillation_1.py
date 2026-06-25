#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_distillation_1.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:33:05 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:33:07 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
