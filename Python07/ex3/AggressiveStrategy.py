from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        sorted_hand = sorted(hand, key=lambda c: c.cost)
        for card in sorted_hand:
            if card.cost < 5 and card.is_playable(10 - mana_used):
                card.play({"available_mana": 10 - mana_used})
                cards_played.append(card.name)
                mana_used += card.cost

                if hasattr(card, "attack"):
                    damage_dealt += card.attack
                else:
                    damage_dealt += card.cost * 2

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda t: t != "Enemy Player")