from ex0.Card import Card
from ex0.CreatureCard import CreatureCard

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:

        game_state["available_mana"] -= self.cost

        res_effect = self.resolve_effect([])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": res_effect["effect"]
        }


    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            return {"effect": f"Deal {self.cost} damage to target"}
        elif self.effect_type == "heal":
            return {"effect": f"Heal {self.cost} health to target"}
        elif self.effect_type == "buff":
            return {"effect": f"Buff target for {self.cost} power"}
        elif self.effect_type == "debuff":
            return {"effect": f"Debuff target for {self.cost} power"}
        else:
            return {"effect": "No effect"}