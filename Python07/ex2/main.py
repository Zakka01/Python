from ex2.EliteCard import EliteCard

print("\n=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")


print()

game_state = {"available_mana": 10}
elite = EliteCard("Arcane Warrior", 3, "Legendary", 5, 3, 4)

print("Playing Arcane Warrior (Elite Card):\n")

print("Combat phase:")
attack_result = elite.attack("Enemy")
print("Attack result:", attack_result)

defense_result = elite.defend(5)
print("Defense result:", defense_result)


print()


print("Magic phase:")
spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
print("Spell cast:", spell_result)
mana_result = elite.channel_mana(3)
print("Mana channel:", mana_result)

print("\nMultiple interface implementation successful!")
