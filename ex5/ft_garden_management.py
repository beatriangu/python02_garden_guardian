"""
Exercise 5: Garden Management System
File: ft_garden_management.py
"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, name: str, water: int = 5, sun: int = 8) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": water, "sun": sun}

    def water_plants(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Unknown plant: {name}")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_manager() -> None:
    manager = GardenManager()

    print("=== Garden Management System ===")

    print("Adding plants to garden...")
    for name, water, sun in (("tomato", 5, 8), ("lettuce", 5, 8), ("", 5, 8)):
        try:
            manager.add_plant(name, water, sun)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    manager.water_plants()

    print("Checking plant health...")
    manager.plants["lettuce"]["water"] = 15
    for name in ("tomato", "lettuce"):
        try:
            manager.check_plant_health(name)
        except ValueError as e:
            print(f"Error checking {name}: {e}")
        except GardenError as e:
            print(f"Error checking {name}: {e}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_manager()
