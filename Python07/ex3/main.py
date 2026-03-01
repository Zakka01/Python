from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("\n=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")

fantasy_card = FantasyCardFactory()
aggrassive = AggressiveStrategy()

print(f"Factory: {fantasy_card.__class__.__name__}")
print(f"Strategy: {aggrassive.get_strategy_name()}")
print(f"Available types: {fantasy_card.get_supported_types()}")

print()

engine = GameEngine()
engine.configure_engine(fantasy_card, aggrassive)

print("Simulating aggressive turn...")
hand = [f"{c.name} ({c.cost})" for c in engine.hand]
print(f"Hand: {hand}")


print()

turn_result = engine.simulate_turn()
print("Turn execution:", turn_result)


print()


report = engine.get_engine_status()
print("Game Report:", report)

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
