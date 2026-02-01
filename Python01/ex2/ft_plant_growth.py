class Plant:
    def	__init__(self, name, height, Age):
        self.name = name
        self.height = height
        self.Age = Age
    def grow(self):
        self.height += 1
    def age(self):
        self.Age += 1
    def get_info(self):
        print(f"{self.name} : {self.height}cm, {self.Age} days old")

def	week_simulation(plants):
	i = 0
	while i < len(plants):
		day = 1
		height_before = plants[i].height
		while day <= 7:
			if day == 1 or day == 7:
				print(f"=== Day {day} ===")
				plants[i].get_info()
			if day != 7:
				plants[i].age()
				plants[i].grow()
			day += 1
		height_after = plants[i].height
		growth = height_after - height_before
		print(f"Growth this week: +{growth}cm")
		i += 1

if __name__ == "__main__":
    plants = [
		Plant("Rose", 25, 30),
		# Plant("flower", 15, 45),
		# Plant("tree", 450, 120)
	]
    week_simulation(plants)
