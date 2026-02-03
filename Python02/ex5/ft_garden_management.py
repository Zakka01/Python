class GardenManager:
    def __init__(self, gardens):
        self.gardens = []
        
    def add_plant(self, plant):
        self.gardens.append(plant)
    
    def water_plant(self, plant):
        print(f"Watering {plant} - success")
    
    def check_plant_health(self, plant):
        pass