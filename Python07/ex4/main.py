from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("'n=== DataDeck Tournament Platform ===\n")

print("Registering Tournament Cards...\n")
dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
wizard = TournamentCard("Ice Wizard", 4, "Epic", 4, 6, 1150)

platform = TournamentPlatform()
dragon_id = platform.register_card(dragon, "dragon_001")
wizard_id = platform.register_card(wizard, "wizard_001")
dragon_info = dragon.get_rank_info()

print(f"Fire Dragon (ID: {dragon_id}):")
print(f"- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {dragon_info['rating']}")
print(f"- Record: {dragon_info['record']}")

print()

wizard_info = wizard.get_rank_info()
print(f"Ice Wizard (ID: {wizard_id}):")
print(f"- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {wizard_info['rating']}")
print(f"- Record: {wizard_info['record']}")

print()

print("Creating tournament match...")
match_result = platform.create_match(dragon_id, wizard_id)
print(f"Match result: {match_result}")

print()

print("Tournament Leaderboard:")
leaderboard = platform.get_leaderboard()
for entry in leaderboard:
    print(f"{entry['rank']}. {entry['name']} - Rating: {entry['rating']} ({entry['record']})")

print()

print("Platform Report:")
report = platform.generate_tournament_report()
print(report)


print()

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")