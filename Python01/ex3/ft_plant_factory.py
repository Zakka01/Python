class Plant:
	def	__init__(self, name, height, Age):
		self.name = name
		self.height = height
		self.Age = Age

	def	get_info(self):
		print(f"Created: {self.name} ({self.height}cm, {self.Age} days)")

def	Factory():
	i = 0
	while i < len(plants):
		plants[i].get_info()
		i += 1
	print(f"\nTotal plants created: {len(plants)}")
	return

if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	plants = [
		Plant("Rose", 25, 30),
		Plant("Oak", 200, 365),
		Plant("Cactus", 5, 90),
		Plant("Sunflower", 80, 45),
		Plant("Fern" ,15, 120)
	]
	Factory()