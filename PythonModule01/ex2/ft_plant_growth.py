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
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
