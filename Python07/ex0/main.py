from CreatureCard import CreatureCard

print("\n=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

# Create a creature card
fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
print("CreatureCard Info:")
print(fire_dragon.get_card_info())


print()


# play
available_mana = 6
print(f"Playing {fire_dragon.name} with {available_mana} mana available:")
print("Playable:", fire_dragon.is_playable(available_mana))
play_result = fire_dragon.play({"available_mana": available_mana})
print("Play result:", play_result)


print()


# Simulate attacking another creature
goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 3)
print(f"{fire_dragon.name} attacks {goblin.name}:")
attack_result = fire_dragon.attack_target(goblin)
print("Attack result:", attack_result)


print()


# Test insufficient mana
insufficient_mana = 3
print(f"Testing insufficient mana ({insufficient_mana} available):")
print("Playable:", fire_dragon.is_playable(insufficient_mana))


print("\nAbstract pattern successfully demonstrated!")