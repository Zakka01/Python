class Garden:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        
    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")
    
    def report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def grow(self):
        self.__height += 1

    def increase_age(self):
        self.__age += 1
    
    def get_info(self):
        print(f"{self.name} Tree: {self.get_height()}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color 
    def bloom(self):
        return f"{self.name} is blooming in {self.color} color!"
   
    def get_info(self):
        print(f"{self.name}: {self.get_height()}cm, {self.color} flowers (blooming)") 

            
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    def show_prize(self):
        print(f"{self.name} has {self.prize_points} prize points!")
    def get_info(self):
        return f"{self.name}: {self.get_height()}cm, {self.get_age()} days, {self.color} flowers (blooming), Prize points: {self.prize_points}"

 
class GardenManager:
    def __init__(self):
        self.gardens = []
        
    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def total_growth(self):
            return sum(plant.get_height() for plant in self.garden.plants)

        def plant_types_count(self):
            regular = flowering = prize = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def add_garden(self, garden):
        self.gardens.append(garden)
        print(f"Added a garden for {garden.owner_name}!")

    def remove_garden(self, index):
        if 0 <= index < len(self.gardens):
            self.gardens.pop(index)
            print(f"Garden at index {index} removed!")
        else:
            print("Invalid index!")
            
    @classmethod
    def create_garden_network(cls):
        manager = cls()
        alice_garden = Garden("Alice")
        bob_garden = Garden("Bob")
        manager.add_garden(alice_garden)
        manager.add_garden(bob_garden)
        return manager

    @staticmethod
    def validate_height(plant):
        return plant.get_height() >= 0

