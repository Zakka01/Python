class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.deck = []
        self.battlefield = []
        self.hand = []

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck = sum(list(factory.create_themed_deck(3).values()), [])
        self.hand = self.deck.copy()

    def simulate_turn(self) -> dict:
        if not self.strategy:
            raise ValueError("Strategy not configured")
        if not self.factory:
            raise ValueError("Factory not configured")

        result = self.strategy.execute_turn(self.hand, self.battlefield)
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": 1,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": (result := self.strategy.execute_turn(self.hand, self.battlefield)),
            "cards_created": len(self.deck)
        }