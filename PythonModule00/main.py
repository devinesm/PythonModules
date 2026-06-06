#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily from the root folder.
Just run: python3 main.py

How it works:
1. It adds the specific exercise folder (e.g., ex00) to the system path temporarily.
2. It tries to import your exercise files (like ft_plot_area.py)
3. It calls your functions to test them
4. If there's an error, it tells you what went wrong
"""

import sys
import os

def test_ft_exercise(exercise_file_name, folder_name):
    """
    This function tries to run one of your exercises from its specific folder.
    """
    print(f"\n=== Testing {exercise_file_name} from {folder_name}/ ===")

    # First, verify if the folder actually exists
    if not os.path.isdir(folder_name):
        print(f"❌ Could not find folder '{folder_name}/'.")
        print(f"   Make sure the folder exists in the same directory as main.py")
        return

    try:
        # Temporarily insert the exercise folder at the start of sys.path
        # This tells Python to look inside this folder FIRST for the import
        sys.path.insert(0, folder_name)

        # Import your exercise file
        ft_module = __import__(exercise_file_name)

        # Get the function from your file
        ft_function = getattr(ft_module, exercise_file_name)

        # Special handling for ft_seed_inventory (Exercise 7)
        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            # Run your function normally (no parameters)
            ft_function()

    except ImportError:
        print(f"❌ Could not find {exercise_file_name}.py in {folder_name}/")
    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}() in your file")
        print(f"   Make sure you have: def {exercise_file_name}():")
    except TypeError as error:
        msg = str(error)
        print(f"❌ Type error: {error}")
        if exercise_file_name == "ft_seed_inventory":
            if "missing" in msg and "required positional argument" in msg:
                print("   For exercise 7, make sure your function takes parameters:")
                print(f"   def {exercise_file_name}(seed_type: str, quantity: int, unit: str) -> None:")
        else:
            print("   Your function should not take any parameters")
    except Exception as error:
        print(f"❌ Error running your function: {error}")
        print("   Check your code for syntax errors")
    finally:
        # CLEANUP: Always remove the folder from sys.path afterwards.
        # This prevents imports from one exercise from messing up another.
        if sys.path and sys.path[0] == folder_name:
            sys.path.pop(0)


def main():
    """Run main function - this runs when you execute: python3 main.py ."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_garden_name      (Display garden name)")
    print("2 - ft_plot_area        (Calculate garden plot area)")
    print("3 - ft_harvest_total    (Add up harvest weights)")
    print("4 - ft_plant_age        (Check if plant is ready)")
    print("5 - ft_water_reminder   (Check if plants need water)")
    print("6 - ft_count_harvest    (Count days to harvest)")
    print("7 - ft_seed_inventory   (Seed inventory with type hints)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    # Test the exercise based on user choice, passing the folder name
    if choice == "0":
        test_ft_exercise("ft_hello_garden", "ex0")
    elif choice == "1":
        test_ft_exercise("ft_garden_name", "ex1")
    elif choice == "2":
        test_ft_exercise("ft_plot_area", "ex2")
    elif choice == "3":
        test_ft_exercise("ft_harvest_total", "ex3")
    elif choice == "4":
        test_ft_exercise("ft_plant_age", "ex4")
    elif choice == "5":
        test_ft_exercise("ft_water_reminder", "ex5")
    elif choice == "6":
        test_ft_exercise("ft_count_harvest_iterative", "ex6")
        test_ft_exercise("ft_count_harvest_recursive", "ex6")
    elif choice == "7":
        test_ft_exercise("ft_seed_inventory", "ex7")
    elif choice == "a":
        # Test all exercises one by one
        test_ft_exercise("ft_hello_garden", "ex0")
        test_ft_exercise("ft_garden_name", "ex1")
        test_ft_exercise("ft_plot_area", "ex2")
        test_ft_exercise("ft_harvest_total", "ex3")
        test_ft_exercise("ft_plant_age", "ex4")
        test_ft_exercise("ft_water_reminder", "ex5")
        test_ft_exercise("ft_count_harvest_iterative", "ex6")
        test_ft_exercise("ft_count_harvest_recursive", "ex6")
        test_ft_exercise("ft_seed_inventory", "ex7")
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")


if __name__ == "__main__":
    main()
