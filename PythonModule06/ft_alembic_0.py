#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_0.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 04:54:59 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 04:55:00 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
