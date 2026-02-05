class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")
    
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
        
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
        
    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")
    
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {harvest_season} harvest")
        print(f"Tomato is rich in {self.nutritional_value}")


if __name__ == "__main__":
	flower = Flower("Rose", 25, 30, "red")
	flower.bloom()
 
	tree = Tree("Oak", 500, 1825, 50)	
	tree.produce_shade()
	
	veg = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    