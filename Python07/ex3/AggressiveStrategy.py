from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        available_mana = 5

        sorted_hand = sorted(hand, key=lambda c: c.cost)
        played_spells = []
        for card in sorted_hand:
            if card.__class__.__name__ == 'ArtifactCard':
                continue
            if card.cost <= available_mana - mana_used:
                cards_played.append(card.name)
                mana_used += card.cost
                if card.__class__.__name__ == 'SpellCard':
                    played_spells.append(card)

        creature_attacks = [getattr(c, 'attack', 0) for c in hand if hasattr(c, 'attack')]
        spell_damage = sum(c.cost for c in played_spells)
        damage_dealt = (max(creature_attacks) if creature_attacks else 0) + spell_damage

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda t: t != "Enemy Player")