"""
Exercise 2: Making Your Own Error Types
File: ft_custom_errors.py
"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def simulate_plant_problem():
    raise PlantError("The tomato plant is wilting!")


def simulate_water_problem():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        simulate_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        simulate_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    for action in (simulate_plant_problem, simulate_water_problem):
        try:
            action()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
