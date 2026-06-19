#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_inventory_system.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 10:46:19 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 11:49:35 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import sys


def parse_args(args: list[str]) -> dict:
    inventory: dict[str, int] = {}

    for item in args[1:]:
        inventory_item = item.split(":")

        try:
            if (len(inventory_item) != 2 or inventory_item[0] == item):
                raise Exception(f"Error - invalid parameter '{item}'")

            name = inventory_item[0]
            qty_str = inventory_item[1]

            if (name in inventory.keys()):
                raise Exception(f"Redundant item '{name}' - discarding")

            try:
                qty = int(qty_str)
            except ValueError as e:
                raise Exception(f"Quantity error for '{name}': {e}")

            inventory.update({name: qty})
        except Exception as e:
            print(f"{e}")
            continue

    return (inventory)


def sort_dict(inventory: dict) -> dict:
    inventory_list = list(inventory.items())
    n = len(inventory_list)

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if inventory_list[j][1] < inventory_list[j + 1][1]:
                temp = inventory_list[j]
                inventory_list[j] = inventory_list[j + 1]
                inventory_list[j + 1] = temp
            j += 1
        i += 1

    return dict(inventory_list)


def update_inventory(inventory: dict, key: str, value: int) -> None:
    return inventory.update({key: value})


def main(args: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_args(args)

    print()
    print(f"Got inventory: {inventory}")

    print()
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.keys())} items: {total}")
    print()
    if (total > 0):
        for item in inventory:
            num = inventory[item]
            print(f"Item {item} represents {num / total * 100:.1f}%")

    sorted_inventory = sort_dict(inventory)

    print()
    least_key = list(sorted_inventory.keys())[len(inventory) - 1]
    least_val = list(sorted_inventory.values())[len(inventory) - 1]
    most_key = list(sorted_inventory.keys())[0]
    most_val = list(sorted_inventory.values())[0]
    print(f"Item most abundant: {most_key} with quantity {most_val}")
    print(f"Item least abundant: {least_key} with quantity {least_val}")
    print()

    update_inventory(inventory, "magic_item", 1)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main(sys.argv)
