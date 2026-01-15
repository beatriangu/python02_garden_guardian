"""
Exercise 0: Agricultural Data Validation Pipeline
File: ft_first_exception.py
"""


def check_temperature(temp_str):
    """
    Tries to convert a string to an integer temperature and checks
    if it is within the valid range for plants (0 to 40 degrees).
    Returns the temperature if valid.
    """
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]
    for i, t in enumerate(tests):
        print(f"Testing temperature: {t}")
        try:
            temp = check_temperature(t)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")

        if i != len(tests) - 1:
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
