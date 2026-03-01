class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def Age(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name} : {self.height}cm, {self.age} days old")


def week_simulation():
    plants = [
        Plant("Rose", 25, 30)
        # Plant("Tulip", 15, 20),
        # Plant("Daisy", 10, 15)
    ]

    print("=== Day 1 ===")
    for i in range(len(plants)):
        plants[i].get_info()

    for day in range(1, 7):
        for plant in plants:
            plant.grow()
            plant.Age()

    print("=== Day 7 ===")
    for i in range(len(plants)):
        plants[i].get_info()
        print("Growth this week: +6cm")


if __name__ == "__main__":
    week_simulation()
