def garden_operations():
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("\nTesting ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("\nTesting FileNotFoundError...")
        filename = "missing.txt"
        open(filename, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{filename}'")

    try:
        print("\nTesting KeyError...")
        garden = {"flower": "white"}
        print(garden["rose"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    try:
        print("\nTesting multiple errors together...")
        int("aa")
        9 / 0
    except Exception:
        print("Caught an error, but program continues!")


def test_error_types():
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
