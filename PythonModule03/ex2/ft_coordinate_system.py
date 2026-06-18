#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_coordinate_system.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/18 16:28:31 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/18 18:56:14 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import math


def parse_args(coordinates: list[str]) -> list[float]:
    coords : list[float] = []

    if (len(coordinates) != 3):
        raise Exception("Invalid syntax")

    i = 0
    while (i < len(coordinates)):
        try:
            coords.append(float(coordinates[i]))
        except Exception:
            raise Exception("Invalid syntax")
        i += 1

    return (coords)


def get_player_pos() -> tuple[float, float, float] :    
    valid = False
    while (valid == False):
        user_input = input("Enter new coordinates as floats in format 'x, y, z': ")
        coordinates: list[str] = user_input.split(",")

        try:
            coords = parse_args(coordinates)
            valid = True
        except Exception as e:
            print(f"{e}")

    return (coords[0], coords[1], coords[2])
    

def display_tuple(coords: tuple[float, float, float]) -> None:
    print(f"Got a first tuple: {coords}")


def display_coords(coords: tuple[float, float, float]) -> None:
    print("It includes: ", end="")
    print(f"X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


# def calculate_distance(coords: tuple[float, float, float], coords2: tuple[float, float, float]) -> float:
#     return (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def main() -> None:
    print("Get a first set of coordinates")
    first_coords = get_player_pos()
    display_tuple(first_coords)
    display_coords(first_coords)
    
    # distance_to_center = calculate_distance(first_coords, (0,0,0))
    # print(f"Distance to center: {distance_to_center}")

    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    # distance_coords = calculate_distance(first_coords, second_coords)
    # print(f"Distance between the 2 sets of coordinates: {distance_coords}")

if __name__ == "__main__":
    main()