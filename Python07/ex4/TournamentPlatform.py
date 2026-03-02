from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches = []

    def register_card(self, card: TournamentCard, card_id: str) -> str:
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = card1, card2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

        self.matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.items(), key=lambda x: x[1].rating, reverse=True)
        leaderboard = []

        for rank, (card_id, card) in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "rating": info["rating"],
                "record": info["record"],
            })

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_rating = sum(c.rating for c in self.cards.values())
        avg_rating = total_rating // total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": len(self.matches),
            "avg_rating": avg_rating,
            "platform_status": "active",
        }