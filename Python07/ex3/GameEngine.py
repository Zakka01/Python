class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.deck = []
        self.battlefield = []
        self.hand = []
        self._last_result = None
        self._turns_simulated = 0

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck = sum(list(factory.create_themed_deck(3).values()), [])
        self.hand = self.deck.copy()

    def simulate_turn(self) -> dict:
        if not self.factory:
            raise RuntimeError("Factory not configured")
        if not self.strategy:
            raise RuntimeError("Strategy not configured")

        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self._last_result = actions
        self._turns_simulated += 1
        return {
            "Strategy": self.strategy.get_strategy_name(),
            "Actions": actions
        }

    def get_engine_status(self) -> dict:
        if not self.strategy:
            raise RuntimeError("Engine not configured")
        total_damage = self._last_result.get("damage_dealt", 0) if self._last_result is not None else 0
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": total_damage,
            "cards_created": len(self.deck)
        }