#!/usr/bin/env python3


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


def main(args: list[str]) -> None:
	print("=== Inventory System Analysis ===")
	inventory = parse_args(args)

	print()
	print(f"Got inventory: {inventory}")

	print()
	print(f"Item list: {list(inventory.keys())}")
	print(f"Total quantity of the {len(inventory.keys())} items: {sum(inventory.values())}")
	print()

	if (sum(inventory.values()) > 0):
		for item in inventory:
			num = inventory[item]
			print(f"Item {item} represents {num / sum(inventory.values()) * 100:.1f}%")


if __name__ == "__main__":
	main(sys.argv)
