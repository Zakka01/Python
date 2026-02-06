class Plant:
    def __init__(self, name: str = "Rose", height: int = 25, age: int = 30):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def Factory():
    plants = [
        Plant(),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    for i in range(len(plants)):
        plants[i].get_info()
    print(f"\nTotal plants created: {len(plants)}")
    return


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Factory()
