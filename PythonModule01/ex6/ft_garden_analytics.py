#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def grow_call(self) -> None:
            self._grow_calls += 1

        def age_call(self) -> None:
            self._age_calls += 1

        def show_calls(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = age
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats.show_calls()
        name = self._name.capitalize()
        print(f"{name}: {self.get_height():.1f}cm, {self.get_age()} days old")

    def grow(self, growth: float) -> None:
        self._stats.grow_call()
        self._height += growth

    def age(self) -> None:
        self._stats.age_call()
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

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True

    def get_color(self) -> str:
        return self._color

    def get_bloom(self) -> bool:
        return self._bloom

    def grow_and_bloom(self, amount: float) -> None:
        print(f"[asking the {self._name} to grow and bloom]")
        self._bloom = True
        self.grow(amount)

    def show(self) -> None:
        super().show()
        print(f"Color: {self.get_color()}")
        if self.get_bloom():
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls: int = 0

        def produce_shade_call(self) -> None:
            self._produce_shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._produce_shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self.TreeStats()

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        if isinstance(self._stats, self.TreeStats):
            self._stats.produce_shade_call()

        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces a shade of"
              f"{self.get_height():.1f}cm long and "
              f"{self.get_trunk_diameter():.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.get_trunk_diameter():.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow_and_age(self, amount: int, grow: float) -> None:
        for _ in range(amount):
            self._nutritional_value += 1
            super().grow(grow)
            super().age()
        print(f"[make {self._name} grow and age for {amount} days]")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.get_harvest_season().capitalize()}")
        print(f"Nutritional value: {self.get_nutritional_value()}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds_bloomed: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds_bloomed = seeds_bloomed

    def get_seeds_bloomed(self) -> int:
        return self._seeds_bloomed

    def seed_grow_age_bloom(self, amount: int, grow_rate: float) -> None:
        print(f"[make {self._name} grow, age and bloom]")

        self.grow(amount * grow_rate)

        self._plant_age += (amount - 1)
        self.age()

        self._bloom = True

        self._seeds_bloomed += int(amount * 2.1)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.get_seeds_bloomed()}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name.capitalize()}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print("Is 400 days more than a year? ->"
          f" {Plant.is_older_than_a_year(400)}")

    print()

    print("=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    display_stats(flower)
    flower.grow_and_bloom(8.0)
    flower.show()
    display_stats(flower)

    print()

    print("=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    tree.produce_shade()
    display_stats(tree)

    print()

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    sunflower.seed_grow_age_bloom(20, 1.5)
    sunflower.show()
    display_stats(sunflower)

    print()

    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()
