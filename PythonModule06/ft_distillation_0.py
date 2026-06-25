#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_distillation_0.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:28:41 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:28:42 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")


if __name__ == "__main__":
    main()
