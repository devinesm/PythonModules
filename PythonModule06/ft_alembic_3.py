#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_3.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:07:44 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:07:45 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from alchemy import elements


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    print(f"Testing create_air: {elements.create_air()}")


if __name__ == "__main__":
    main()
