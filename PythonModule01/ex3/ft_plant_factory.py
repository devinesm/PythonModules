#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


def main():
    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
