#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = age

    def show(self) -> None:
        name = self._name.capitalize()
        print(f"{name}: {self._height:.1f}cm, {self._plant_age} days old")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._plant_age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self.get_height():.1f}cm")
        else:
            print(f"{self._name.capitalize()}: "
                  "Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days: int) -> None:
        if days >= 0:
            self._plant_age = days
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")


def main():
    print("=== Garden Security System ===")

    plant = Plant("rose", 15, 10)

    print("Plant created: ", end="")
    plant.show()

    print()

    plant.set_height(25)
    plant.set_age(30)

    print()

    plant.set_height(-1)
    plant.set_age(-1)

    print()

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
