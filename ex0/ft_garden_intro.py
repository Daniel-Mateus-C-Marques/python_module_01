#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 14:45:43 by danicamp            #+#    #+#            #
#   Updated: 2026/06/19 14:45:50 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_garden_intro() -> None:
    plant: str = "Rose"
    height: float = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.capitalize()}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
