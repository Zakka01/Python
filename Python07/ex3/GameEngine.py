class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.deck = []
        self.battlefield = []
        self.hand = []
        self._last_turn_result = None
        self.turns = 0

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

        self._last_turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns += 1
        return self._last_turn_result

    def get_engine_status(self) -> dict:
        damage = self._last_turn_result.get("damage_dealt", 0) if self._last_turn_result else 0
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": damage,
            "cards_created": len(self.deck),
        }