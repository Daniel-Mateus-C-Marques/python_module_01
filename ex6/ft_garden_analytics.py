#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/24 16:02:20 by danicamp            #+#    #+#            #
#   Updated: 2026/06/26 12:49:52 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    class Statistics:
        n_age: int = 0
        n_grow: int = 0
        n_show: int = 0
        n_shade: int = 0

        def increment_age(self) -> None:
            self.n_age += 1

        def increnet_grow(self) -> None:
            self.n_grow += 1

        def increnet_show(self) -> None:
            self.n_grow += 1

        def statistics_show(self) -> None:
            print(f"Stats: {self.n_grow} grow, {self.n_age} age, "
                  f"{self.n_show} show")

    def __init__(self, name: str, height: float, age: int, size_grow: float):
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.size_grow: float = size_grow
        self.statistic = Plant.Statistics()

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.plant_age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.plant_age = age
            print(f"Age updated: {self.plant_age} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm")

    def show(self) -> None:
        self.statistic.n_show += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.statistic.n_grow += 1
        self.height += self.size_grow

    def age(self) -> None:
        self.statistic.n_age += 1
        self.plant_age += 1

    @staticmethod
    def more_than_year(age: int) -> str:
        if age > 365:
            return "True"
        else:
            return "False"

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unkown plant", 0, 0, 0)


class Flower(Plant):

    class Seed:
        n_seed = 0

        def seed_show(self) -> None:
            print(f"Seeds: {self.n_seed}")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        size_grow: float,
        color: str
    ):
        super().__init__(name, height, age, size_grow)
        self.color = color
        self.seeds = Flower.Seed()

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")
        self.seeds.n_seed += 42


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        size_grow: float,
        trunk_diameter: float
    ):
        super().__init__(name, height, age, size_grow)
        self.trunk_diameter = trunk_diameter

    def statistics_show(self) -> None:
        self.statistic.statistics_show()
        print(f"{self.statistic.n_shade} shade")

    def produce_shade(self) -> None:
        self.statistic.n_shade += 1
        print(f"Tree Oak now produces a shade of {self.height:.1f} "
              f"long and {self.trunk_diameter:.1f} wide."
              )


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    age: int = 30
    age2: int = 400
    print(f"Is {age} days more than a year? -> {Plant.more_than_year(age)}")
    print(f"Is {age2} days more than a year? -> {Plant.more_than_year(age2)}")
    print("")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, 8, "red")
    flower.show()
    print(f"Color: {flower.color}")
    print("Rose has not bloomed yet")
    print("[statistics for Rose]")
    flower.statistic.statistics_show()
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.show()
    print(f"Color: {flower.color}")
    flower.bloom()
    flower.statistic.statistics_show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 10, 5)
    print(f"Trunk diameter: {oak.trunk_diameter:.1f}")
    print("[statistics for Oak]")
    oak.statistics_show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.statistics_show()
    print("")
    print("=== Seed")
    flower2 = Flower("Sunflower", 80, 45, 1.5, "yellow")
    flower2.show()
    print(f"Color: {flower2.color}")
    print("Sunflower has not bloomed yet")
    flower2.seeds.seed_show()
    print("[make sunflower grow, age and bloom]")
    for i in range(20):
        flower2.age()
        flower2.grow()
    flower2.show()
    print(f"Color: {flower2.color}")
    flower2.bloom()
    flower2.seeds.seed_show()
    print("[statistics for Sunflower]")
    flower2.statistic.statistics_show()
    print("")
    print("=== Anonymous")
    unkown = Plant.anonymous()
    unkown.show()
    print("[statistics for Unknown plant]")
    unkown.statistic.statistics_show()


if __name__ == "__main__":
    ft_garden_analytics()
