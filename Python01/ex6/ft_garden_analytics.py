class Garden:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = [] 

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")
        
    def grow_all(self, plants):
        i = 0
        print(f"\n{self.owner_name} is helping all plants grow...")
        while i < len(plants):
            plants[i].grow()
            print(f"{plants[i].name} grew 1cm")
            i += 1
            
    def report(self, plants):
        i = 0
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        while i < len(plants):
            print(f"- {plants[i].get_info()}")
            i += 1


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        self.__growth = 0
    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age
    def get_growth(self):
        return self.__growth
    def grow(self):
        self.__height += 1
        self.__growth += 1
    def get_info(self):
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def get_info(self):
        return f"{self.name}: {self.get_height()}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    def get_info(self):
        return f"{self.name}: {self.get_height()}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}"


class GardenManager:
    def __init__(self):
        self.gardens = []
        
    def total_gardens(self):
        return len(self.gardens)
    
    def garden_score(self, garden):
        score = 0
        for plant in garden.plants:
            score += plant.get_height()
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score
    
    class GardenStats:
        def __init__(self, garden):
            self.garden = garden
        
        def plants_count(self):
            return len(self.garden.plants)

        def total_growth(self):
            total = 0
            i = 0
            while i < len(self.garden.plants):
                total += self.garden.plants[i].get_growth()
                i += 1
            return total

        def plant_types_count(self):
            regular = flowering = prize = i = 0
            while i < len(self.garden.plants):
                if isinstance(self.garden.plants[i], PrizeFlower):
                    prize += 1
                elif isinstance(self.garden.plants[i], FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
                i += 1
            return f"{regular} regular, {flowering} flowering, {prize} prize flowers"\
        
        def valid_height(self):
            i = 0
            while i < len(self.garden.plants):
                if self.garden.plants[i].get_height() < 0:
                    return False
                i += 1
            return True
    
    

if __name__ == "__main__":
    print("== Garden Management System Demo ==\n")
    
    alice = Garden("Alice")
    bob = Garden("Bob")

    oak = Plant("Oak Tree", 100, 5)
    rose = FloweringPlant("Rose", 25, 2, "red")
    sunflower = PrizeFlower("Sunflower", 50, 3, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    
    alice.grow_all(alice.plants)

    alice.report(alice.plants)
    bob.report(bob.pla)

    manager = GardenManager()
    manager.gardens.append(alice)
    manager.gardens.append(bob)
    stats = GardenManager.GardenStats(alice)
    

    print(f"\nPlants added: {stats.plants_count()}, Total growth: {stats.total_growth()}")
    print("Plant types:", stats.plant_types_count())
    
    print(f"\nHeight validation test: {stats.valid_height()}")
    
    print(f"Garden scores - Alice: {manager.garden_score(alice)}, Bob: {manager.garden_score(bob)}")
    print(f"Total gardens managed: {manager.total_gardens()}")
