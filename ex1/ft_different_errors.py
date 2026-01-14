"""
Exercise 1: Different Types of Problems
File: ft_different_errors.py
"""


def garden_operations():
    """
    Demonstrates common Python error types that can happen in a garden program.
    """
    tests = [
        ("ValueError", lambda: int("abc")),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("FileNotFoundError", lambda: open("missing.txt", "r")),
        ("KeyError", lambda: {"tomato": 10}["missing_plant"]),
    ]

    for i, (name, action) in enumerate(tests):
        print(f"Testing {name}...")
        try:
            action()
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except KeyError as e:
            print(f"Caught KeyError: {e}")

        if i != len(tests) - 1:
            print()


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()

    garden_operations()

    print()
    print("Testing multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()


