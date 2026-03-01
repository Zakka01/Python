from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                attack_power: int, defense: int, mana_pool: int):
        super().__init__(name, cost, rarity)

        self.attack_power = attack_power
        self.defense = defense
        self.mana_pool = mana_pool
        self.health = 10

    def play(self, game_state: dict) -> dict:
        if game_state["available_mana"] < self.cost:
            return {"error": "Not enough mana"}

        game_state["available_mana"] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 4

        if self.mana_pool < mana_cost:
            return {"error": "Not enough mana"}

        self.mana_pool -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount

        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool
        }