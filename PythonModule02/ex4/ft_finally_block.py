#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_finally_block.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/18 14:38:49 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/18 14:48:10 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(
            "Invalid plant name to water: "
            f"'{plant_name}'"
        )
    print(f"Watering {plant_name}: [OK]")


def test(inputs: list[str]) -> None:
    print("Opening watering system")
    try:
        water_plant(inputs[0])
        water_plant(inputs[1])
        water_plant(inputs[2])
    except PlantError as plant_error:
        print(f"Caught PlantError: {plant_error}")
        print("...ending tests and returning to main")
    finally:
        print("Closing watering system")


def test_watering_system(
    first_inputs: list[str],
    last_inputs: list[str],
) -> None:
    print("Testing valid plants...")
    test(first_inputs)

    print()

    print("Testing invalid plants...")
    test(last_inputs)


def main() -> None:
    print("=== Garden Watering System ===")

    print()

    first_inputs = ["Tomato", "Lettuce", "Carrots"]
    last_inputs = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(first_inputs, last_inputs)

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
