from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("\n=== DataDeck Deck Builder ===\n")

deck = Deck()

# Add different cards
deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
deck.add_card(ArtifactCard("Mana Crystal", 4, "Rare", 5, "+1 mana per turn"))
deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

deck.shuffle()

# Show stats
print("Building deck with different card types...")
print("Deck stats:", deck.get_deck_stats())



# Drawing and playing cards
print("\nDrawing and playing cards:\n")

game_state = {"available_mana": 10}
while deck.cards:

    card = deck.draw_card()

    if card.__class__.__name__ == "CreatureCard":
        card_type = "Creature"
    elif card.__class__.__name__ == "SpellCard":
        card_type = "Spell"
    elif card.__class__.__name__ == "ArtifactCard":
        card_type = "Artifact"

    print(f"Drew: {card.name} ({card_type})")
    result = card.play(game_state)
    print("Play result:", result)
    print()

print("Polymorphism in action: Same interface, different card behaviors!")