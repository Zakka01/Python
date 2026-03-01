print("\n=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
import alchemy.elements
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}") # longer not clean code | good large project

print("\nMethod 2 - Specific function import:")
from alchemy.elements import create_water
print(f"create_water(): {create_water()}") # hard knowing where it comes from | name conflict

print("\nMethod 3 - Aliased import:")
from alchemy.potions import healing_potion as heal  # good if org name is long , clean | reduce readability if unclear
print(f"heal(): {heal()}")

print("\nMethod 4 - Multiple imports:")
from alchemy.elements import create_earth, create_fire # direct access, good when need few func | but can clutter the fjle
from alchemy.potions import strength_potion # make the file charge and full | name conflict 
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")

print("\nAll import transmutation methods mastered!")