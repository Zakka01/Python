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
        return (
            f"{self.name}: {self.get_height()}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    def total_gardens(self):
        return len(self.gardens)

    def garden_score(self, garden):
        score = 0
        for plant in garden.plants:
            score += plant.get_height()
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_owner_name(name):
        return isinstance(name, str) and len(name.strip()) > 0

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def plants_count(self):
            return len(self.garden.plants)

        def total_growth(self):
            return sum(p.get_growth() for p in self.garden.plants)

        def plant_types_count(self):
            regular = flowering = prize = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return f"{regular} regular, {flowering} flowering, {prize} prize flowers"

        def valid_height(self):
            return all(p.get_height() >= 0 for p in self.garden.plants)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = Garden("Alice")
    bob = Garden("Bob")

    oak = Plant("Oak Tree", 100, 5)
    rose = FloweringPlant("Rose", 25, 2, "red")
    sunflower = PrizeFlower("Sunflower", 50, 3, "yellow", 10)

    bob_plant = Plant("Pine Tree", 92, 4)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()

    alice.report()

    manager = GardenManager.create_garden_network()
    manager.add_garden(alice)
    manager.add_garden(bob)

    bob.add_plant(bob_plant)

    stats = GardenManager.GardenStats(alice)

    print(f"Plants added: {stats.plants_count()}, Total growth: {stats.total_growth()}cm")
    print("Plant types:", stats.plant_types_count())
    print(f"Height validation test: {stats.valid_height()}")
    print(f"Garden scores - Alice: {manager.garden_score(alice)}, Bob: {manager.garden_score(bob)}")
    print(f"Total gardens managed: {manager.total_gardens()}")