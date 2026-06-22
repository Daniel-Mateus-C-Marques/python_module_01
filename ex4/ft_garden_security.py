#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:22:24 by danicamp            #+#    #+#            #
#   Updated: 2026/06/22 16:03:38 by danicamp           ###   ########.fr      #
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


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10, 0.8)
    print("Plant created: ", end="")
    plant.show()
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-2)
    plant.set_age(-30)
    print("")
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
