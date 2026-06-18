#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def custom_error_plant(plant: str) -> None:
    raise PlantError(f"The {plant} plant is wilting!")


def custom_error_water(water: int) -> None:
    if water < 5:
        raise WaterError("Not enough water in tank!")


def custom_error_garden(plant: str, water: int) -> None:
    try:
        custom_error_plant(plant)
    except GardenError as garden_error:
        print(f"Caught {garden_error.__class__.__name__}: {garden_error}")

    try:
        custom_error_water(water)
    except GardenError as garden_error:
        print(f"Caught {garden_error.__class__.__name__}: {garden_error}")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        custom_error_plant("tomato")
    except PlantError as plant_error:
        print(f"Caught {plant_error.__class__.__name__}: {plant_error}")

    print()

    print("Testing WaterError...")
    try:
        custom_error_water(3)
    except WaterError as water_error:
        print(f"Caught {water_error.__class__.__name__}: {water_error}")

    print()

    print("Testing catching all garden errors...")
    custom_error_garden("tomato", 3)

    print()
    print("All custom error types work correctly!")


def main() -> None:
    ft_custom_errors()


if __name__ == "__main__":
    main()
