from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        try:
            cards_played = []
            mana_used = 0
            targets_attacked = []
            damage_dealt = 0

            # Play low-cost creatures first
            sorted_hand = sorted(hand, key=lambda c: getattr(c, "cost", 0))
            for card in sorted_hand:
                if hasattr(card, "is_playable") and card.is_playable(available_mana=10 - mana_used):
                    result = card.play({"available_mana": 10 - mana_used})
                    cards_played.append(card.name)
                    mana_used += result.get("mana_used", 0)

            # Attack enemy player
            for card in battlefield + cards_played:
                targets_attacked.append("Enemy Player")
                damage_dealt += getattr(card, "attack", 4)  # simple default attack

            return {
                "Strategy": self.get_strategy_name(),
                "Actions": {
                    "cards_played": cards_played,
                    "mana_used": mana_used,
                    "targets_attacked": targets_attacked,
                    "damage_dealt": damage_dealt
                }
            }

        except Exception as e:
            return {"error": str(e)}

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        # Prioritize enemy player first
        return sorted(available_targets, key=lambda t: t != "Enemy Player")