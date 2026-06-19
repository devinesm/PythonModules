#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_archive_creation.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 13:34:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 17:46:12 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import sys


def print_data(data: str) -> None:
    print("---")
    print()
    print(data)
    print()
    print("---")


def transform_data(data: str) -> str:
    lines = data.split("\n")
    new_lines = [line + "#" for line in lines
                 if line != ""]
    return "\n".join(new_lines)


def open_file(filename: str) -> str:
    try:
        print(f"Accessing file '{filename}'")
        f = open(filename, "r")
        data = f.read()
        print_data(data)
        f.close()
        print(f"File '{filename}' closed.")
        return (data)
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return ""


def save_data(filename: str, content: str) -> None:
    try:
        f = open(filename, "w")
        f.write(content)
        f.close()
        print(f"Data saved in file '{filename}'")
    except Exception as e:
        print(f"Error saving file '{filename}': {e}")


def main(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    data = open_file(args[1])
    if data == "":
        return

    print()

    print("Transform data:")
    data2 = transform_data(data)
    print_data(data2)

    new_file = str(input("Enter new file name (or empty): "))
    if (new_file == ""):
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file}'")
        save_data(new_file, data2)


if __name__ == "__main__":
    main(sys.argv)
