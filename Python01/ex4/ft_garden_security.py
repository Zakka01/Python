class SecurePlant:
    def __init__(self, name = "Rose", height = 25, age = 30):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, new_height):
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age
    
    def get_info(self):
        print(f"\nCurrent plant: {self.name} ({self.__height}cm, {self.__age} days)")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant()
    plant.set_age(20)
    plant.set_height(12)
    plant.get_info()