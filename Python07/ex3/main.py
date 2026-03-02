from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("\n=== DataDeck Game Engine ===\n")
print("Configuring Fantasy Card Game...")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

print()

engine = GameEngine()
engine.configure_engine(factory, strategy)

print("Simulating aggressive turn...")
hand = [f"{card.name} ({card.cost})" for card in engine.hand]
print(f"Hand: {hand}")


print()

turn_result = engine.simulate_turn()
print("Turn execution:")
print(f"Strategy: {strategy.__class__.__name__}")
print(f"actions: {turn_result}")



print()


report = engine.get_engine_status()
print("Game Report: \n", report)

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
