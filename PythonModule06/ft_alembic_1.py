#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_1.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 04:57:41 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 04:57:42 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
