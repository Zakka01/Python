class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass
        
class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.gardens = []
        
    def add_plant(self, plant):
        try:
            if plant == "" or plant == None:
                raise PlantError("Plant name cannot be empty!")
            else:
                self.gardens.append(plant)
                print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")
    
    
    def water_plant(self, plant):
        if plant not in self.gardens:
            raise WaterError(f"Plant '{plant}' not found in garden!") 
        print(f"Watering {plant} - success")

    
    def check_plant_health(self, plant, water_amount, sunlight_hours):
        try:
            if water_amount < 1:
                raise WaterError(f"Water level {water_amount} is too low (min 1)")
            elif water_amount > 10:
                raise WaterError(f"Water level {water_amount} is too high (max 10)")
            if sunlight_hours < 2:
                raise WaterError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
            elif sunlight_hours > 12:
                raise WaterError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
            else:
                print(f"{plant}: healthy (water: {water_amount}, sun: {sunlight_hours})")
        except WaterError as e:
            print(f"Error checking {plant}: {e}")
            
def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    try:
        print("Opening watering system")
        for i in range(len(manager.gardens)):
            manager.water_plant(manager.gardens[i])
    except GardenError as e:
        print(f"Error watering plants: {e}")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management()