#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 16:03:29 by danicamp            #+#    #+#            #
#   Updated: 2026/06/24 14:42:28 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int, size_grow: float):
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.size_grow: float = size_grow

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
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += self.size_grow

    def age(self) -> None:
        self.plant_age += 1


class Flower(Plant):
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

    def bloom(self) -> None:
        print("Rose is blooming beautifully!")


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

    def produce_shade(self) -> None:
        print(f"Tree Oak now produces a shade of {self.height:.1f} "
              f"long and {self.trunk_diameter:.1f} wide."
              )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        size_grow: float,
        harvest_season: str,
        nutritional_value: float,
    ):
        super().__init__(name, height, age, size_grow)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, 0.8, "red")
    flower.show()
    print(f"Color: {flower.color}")
    print("Rose has not bloomed yet")
    print("[asking the rose to bloom]")
    flower.show()
    print(f"Color: {flower.color}")
    flower.bloom()
    print("")
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 1, 5)
    tree.show()
    print(f"Trunk diameter: {tree.trunk_diameter:.1f}cm")
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("")
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5, 10, 2.1, "April", 0)
    print(f"Harvest season: {vegetable.harvest_season}")
    print(f"Nutritional value: {vegetable.nutritional_value:.0f}")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        vegetable.age()
        vegetable.grow()
    vegetable.show()
    print(f"Harvest season: {vegetable.harvest_season}")
    print(f"Nutritional value: {vegetable.nutritional_value:.0f}")


if __name__ == "__main__":
    ft_plant_types()
