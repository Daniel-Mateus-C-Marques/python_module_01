#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 14:45:58 by danicamp            #+#    #+#            #
#   Updated: 2026/06/22 12:25:10 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    name: str
    height: float
    age: int

    def show(Plant) -> None:
        print(f"{Plant.name}: {Plant.height}cm, {Plant.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    plant = Plant()
    plant.name = "Rose"
    plant.height = 25
    plant.age = 30
    plant2 = Plant()
    plant2.name = "Sunflower"
    plant2.height = 80
    plant2.age = 45
    plant3 = Plant()
    plant3.name = "Cactus"
    plant3.height = 15
    plant3.age = 120
    plant.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
