#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    potions.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ipinto-m <ipinto-m@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 05:22:25 by ipinto-m          #+#    #+#              #
#    Updated: 2026/06/25 05:22:26 by ipinto-m         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    return (f"Healing potion brewed with '{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with '{create_fire()}' and '{create_water()}'")
