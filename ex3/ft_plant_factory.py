#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:03:57 by danicamp            #+#    #+#            #
#   Updated: 2026/06/22 13:18:35 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int, size_grow: float):
        self.name: str = name
        self.height: float = height
        self.plant_age: int = age
        self.size_grow: float = size_grow

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += self.size_grow

    def age(self) -> None:
        self.plant_age += 1


def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25, 30, 0.8)
    plant2 = Plant("Oak", 200, 365, 2.5)
    plant3 = Plant("Cactus", 5, 90, 0.2)
    plant4 = Plant("Sunflower", 80, 45, 0.6)
    plant5 = Plant("Fern", 15, 120, 0.3)
    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    ft_plant_factory()
