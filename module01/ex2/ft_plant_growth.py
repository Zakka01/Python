class Plant:
	def __init__(self, name, height, Age):
		self.name = name
		self.height = height
		self.Age = Age
  
	def grow(self):
		self.height += 1

	def age(self):
		self.Age += 1

	def get_info(self):
		print(f"{self.name} : {self.height}cm, {self.Age} days old")


def	week_simulation():
	Plant_1 = Plant("Rose", 25, 30)
	day = 1
	height_before = Plant_1.height
 
	while day <= 7:
		if day == 1 or day == 7:
			print(f"=== Day {day} ===")
			Plant_1.get_info()
		if day != 7:
			Plant_1.age()
			Plant_1.grow()
		day += 1

	height_after = Plant_1.height
	growth = height_after - height_before
	print(f"Growth this week: +{growth}cm")

if __name__ == "__main__":
	week_simulation()
