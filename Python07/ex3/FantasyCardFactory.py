from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creature_types = ["dragon", "goblin"]
        self.spell_types = ["fireball"]
        self.artifact_types = ["mana_ring"]

    def create_creature(self, name_or_power=None) -> Card:
        if name_or_power is None:
            name_or_power = "Goblin Warrior"

        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> Card:
        if name_or_power is None:
            name_or_power = "Lightning Bolt"

        card = SpellCard("Lightning Bolt", 3, "Common", "damage")
        card.is_playable = lambda available_mana: available_mana >= card.cost
        return card

    def create_artifact(self, name_or_power=None) -> Card:
        if name_or_power is None:
            name_or_power = "Mana Crystal"

        card = ArtifactCard("Mana Crystal", 4, "Rare", 5, "+1 mana per turn")
        card.is_playable = lambda available_mana: available_mana >= card.cost
        return card

    def create_themed_deck(self, size: int) -> dict:
        deck = {
            "creatures": [self.create_creature(t) for t in self.creature_types][:size],
            "spells": [self.create_spell(t) for t in self.spell_types][:size],
            "artifacts": [self.create_artifact(t) for t in self.artifact_types][:size],
        }
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": self.creature_types,
            "spells": self.spell_types,
            "artifacts": self.artifact_types
        }