class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)        

class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)
        

def simulate():
    print("=== Custom Garden Errors Demo ===")
    
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
         
    print("\nTesting catching all garden errors...")
    for error in (PlantError("The tomato plant is wilting!"), 
                WaterError("Not enough water in the tank!")):
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")
        
    print("\nAll custom error types work correctly!")
        
simulate()