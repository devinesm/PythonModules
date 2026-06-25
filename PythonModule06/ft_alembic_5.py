#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_5.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:18:05 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:18:06 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy import create_air

def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
