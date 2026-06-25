#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_4.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:10:58 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:11:01 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    main()
