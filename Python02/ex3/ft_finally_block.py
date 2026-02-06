def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant == None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===")
    
    print("\nTesting normal watering...")
    plants = ["rose", "flower", "oak"]
    water_plants(plants)
    print("Watering completed successfully!")
    
    print("\nTesting with error...")
    plantss = ["Tomato", None]
    water_plants(plantss)
    
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()