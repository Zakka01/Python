from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self._types = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self, name_or_power=None):
        if name_or_power == "dragon" or name_or_power is None:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 3)
        else:
            raise ValueError(f"Unknown creature: {name_or_power}")

    def create_spell(self, name_or_power=None):
        if name_or_power == "fireball" or name_or_power is None:
            return SpellCard("Lightning Bolt", 3, "Common", "damage")
        else:
            raise ValueError(f"Unknown spell: {name_or_power}")

    def create_artifact(self, name_or_power=None):
        if name_or_power == "mana_ring" or name_or_power is None:
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana per turn")
        else:
            raise ValueError(f"Unknown artifact: {name_or_power}")

    def create_themed_deck(self, size: int) -> dict:
        if size < 1:
            raise ValueError("Deck size must be at least 1")
        deck = {
            "creatures": [self.create_creature("dragon"), self.create_creature("goblin")],
            "spells": [self.create_spell("fireball")],
        }
        return deck

    def get_supported_types(self) -> dict:
        return self._types