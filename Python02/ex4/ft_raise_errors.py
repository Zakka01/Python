def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if plant_name == "" or plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except Exception as error:
        print(f"Error : {error}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("Rose", 6, 10)

    print("\nTesting empty plant name...")
    check_plant_health("", 6, 10)

    print("\nTesting bad water level...")
    check_plant_health("Rose", 15, 10)

    print("\nTesting bad sunlight hours...")
    check_plant_health("Rose", 5, 0)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
