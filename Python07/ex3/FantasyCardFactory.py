import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creature_types = ["dragon", "goblin"]
        self.spell_types = ["fireball"]
        self.artifact_types = ["mana_ring"]

    def create_creature(self, name_or_power=None):
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Rare", 5, 4)

    def create_spell(self, name_or_power=None):
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 2, "Uncommon", 3, "Gain 1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        return {
            "creatures": [self.create_creature(t) for t in self.creature_types],
            "spells": [self.create_spell(t) for t in self.spell_types],
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": self.creature_types,
            "spells": self.spell_types,
            "artifacts": self.artifact_types
        }