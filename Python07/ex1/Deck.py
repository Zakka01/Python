from ex0.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []


    def add_card(self, card: Card) -> None:
        self.cards.append(card)


    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False


    def shuffle(self) -> None:
        random.shuffle(self.cards)


    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop(0)


    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        types = {"creatures": 0, "spells": 0, "artifacts": 0}
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            card_type = card.__class__.__name__
            if card_type == "CreatureCard":
                types["creatures"] += 1
            elif card_type == "SpellCard":
                types["spells"] += 1
            elif card_type == "ArtifactCard":
                types["artifacts"] += 1

        if total_cards > 0:
            avg_cost = total_cost / total_cards
        else:
            avg_cost = 0

        stats = {"total_cards": total_cards, **types, "avg_cost": round(avg_cost, 1)}
        return stats

