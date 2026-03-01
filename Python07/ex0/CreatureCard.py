from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health


    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("available_mana", 0)):
            return {"error": "Not enough mana to play this card"}

        game_state["available_mana"] -= self.cost
        
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }


    def attack_target(self, target: object) -> dict:
        try:
            target.health -= self.attack
            if target.health < 0:
                target.health = 0

            return {
                "attacker": self.name,
                "target": getattr(target, "name", str(target)), 
                "damage_dealt": self.attack, 
                "combat_resolved": True
            }
        except AttributeError:
            return {"error": "Invalid target"}


    def get_card_info(self):
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info
