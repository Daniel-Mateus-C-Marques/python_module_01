#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 14:59:06 by danicamp            #+#    #+#            #
#   Updated: 2026/06/19 15:41:29 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1.ft_garden_data import Plant


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25.0, 30, 0.8)
    for i in range(7):
        if i != 0:
            plant.show()
        else:
            plant.age()
            plant.grow()
            plant.show()
