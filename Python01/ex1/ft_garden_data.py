class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_data(self):
        print(f"{self.name} : {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.print_data()
    flower = Plant("Sunflower", 80, 40)
    flower.print_data()
    tree = Plant("Cactus", 15, 120)
    tree.print_data()