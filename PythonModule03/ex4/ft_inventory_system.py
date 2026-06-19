#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_inventory_system.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 10:46:19 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 13:08:31 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import sys


def parse_args(args: list[str]) -> dict:
    loot_dict: dict[str, int] = {}

    i = 1
    while i < len(args):
        current_arg = args[i]
        split_item = current_arg.split(":")

        try:
            if len(split_item) != 2 or split_item[0] == current_arg:
                raise Exception(f"Error - invalid parameter '{current_arg}'")

            item_name = split_item[0]
            val_str = split_item[1]

            if item_name in loot_dict.keys():
                raise Exception(f"Redundant item '{item_name}' - discarding")

            try:
                item_qty = int(val_str)
            except ValueError as err:
                raise Exception(f"Quantity error for '{item_name}': {err}")

            loot_dict.update({item_name: item_qty})
        except Exception as error_msg:
            print(error_msg)

        i += 1

    return loot_dict


def main(args: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    my_inventory = parse_args(args)

    print(f"Got inventory: {my_inventory}")

    item_names = list(my_inventory.keys())
    print(f"Item list: {item_names}")

    total_qty = sum(my_inventory.values())
    print(f"Total quantity of the {len(item_names)} items: {total_qty}")

    if total_qty > 0:
        for name in my_inventory:
            amount = my_inventory[name]
            print(f"Item {name} represents "
                  f"{round((amount / total_qty) * 100, 1):.1f}%")

    if len(item_names) > 0:
        max_item = item_names[0]
        max_amount = my_inventory[max_item]
        min_item = item_names[0]
        min_amount = my_inventory[min_item]

        idx = 1
        while idx < len(item_names):
            current_key = item_names[idx]
            current_val = my_inventory[current_key]

            if current_val > max_amount:
                max_amount = current_val
                max_item = current_key
            if current_val < min_amount:
                min_amount = current_val
                min_item = current_key

            idx += 1

        print(f"Item most abundant: {max_item} with quantity {max_amount}")
        print(f"Item least abundant: {min_item} with quantity {min_amount}")

    my_inventory.update({"magic_item": 1})
    print(f"Updated inventory: {my_inventory}")


if __name__ == "__main__":
    main(sys.argv)
