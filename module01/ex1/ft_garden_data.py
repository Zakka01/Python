class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def print_data(self):
		print(f"{self.name} : {self.height}cm, {self.age} days old")