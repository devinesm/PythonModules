#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_command_quest.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/18 14:57:51 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/18 15:29:19 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def main(args: list[str]) -> None:
    print("=== Command Quest ===")

    print(f"Program name: {args[0]}")

    if (len(args) == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")

        i = 1
        while (i < len(args)):
            print(f"Argument {i}: {args[i]}")
            i += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main(sys.argv)
