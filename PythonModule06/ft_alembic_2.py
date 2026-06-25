#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_2.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:00:30 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:00:31 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
