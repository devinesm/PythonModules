#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_ancient_text.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 13:34:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 17:39:30 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import sys
import typing


def open_file(filename: str) -> None:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO = open(filename, "r")
        print("---")
        print()
        content = f.read()
        print(content)
        print()
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def main(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    open_file(args[1])


if __name__ == "__main__":
    main(sys.argv)
