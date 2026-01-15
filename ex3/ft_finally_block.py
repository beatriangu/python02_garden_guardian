"""
Exercise 3: Finally Block - Always Clean Up
File: ft_finally_block.py
"""


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    ok = water_plants(["tomato", "lettuce", "carrots"])
    if ok:
        print("Watering completed successfully!")
    print()
    print("Testing with error...")
    ok = water_plants(["tomato", None, "carrots"])
    if not ok:
        print()
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
