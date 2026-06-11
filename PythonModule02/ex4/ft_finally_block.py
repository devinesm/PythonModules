#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error") -> None:
		super().__init__(message)


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error") -> None:
		super().__init__(message)


class WaterError(GardenError):
	def __init__(self, message: str = "Unknown water error") -> None:
		super().__init__(message)


def water_plant(plant_name: str) -> None:
	if (plant_name != plant_name.capitalize()):
		raise(PlantError(f"Invalid plant name to water: '{plant_name}'"))
	print(f"Watering {plant_name}: [OK]")


def test_watering_system(first_inputs: list[str], last_inputs: list[str]) -> None:
	print("Testing valid plants...")
	print("Opening watering system")
	try:
		water_plant(first_inputs[0])
		water_plant(first_inputs[1])
		water_plant(first_inputs[2])
	except PlantError as plant_error:
		print(f"Caught PlantError: {plant_error}")
		print("...ending tests and returning to main")
		return
	finally:
		print("Closing watering system")

	print()

	print("Testing invalid plants...")
	print("Opening watering system")
	try:
		water_plant(last_inputs[0])
		water_plant(last_inputs[1])
		water_plant(last_inputs[2])
	except PlantError as plant_error:
		print(f"Caught PlantError: {plant_error}")
		print("...ending tests and returning to main")
		return
	finally:
		print("Closing watering system")

	print("Cleanup always happens, even with errors!")

def main() -> None:
	print("=== Garden Watering System ===")

	print()

	first_inputs = ["Tomato", "Lettuce", "Carrots"]
	last_inputs = ["Tomato", "lettuce", "Carrots"]
	test_watering_system(first_inputs, last_inputs)

if __name__ == "__main__":
	main()
