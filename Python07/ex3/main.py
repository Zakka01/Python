import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===")
print("Configuring Fantasy Card Game...")

fantasy_card = FantasyCardFactory()
aggressive = AggressiveStrategy()

print(f"Factory: {fantasy_card.__class__.__name__}")
print(f"Strategy: {aggressive.get_strategy_name()}")
print(f"Available types: {fantasy_card.get_supported_types()}")

print()

engine = GameEngine()
engine.configure_engine(fantasy_card, aggressive)

print("Simulating aggressive turn...")
print()

hand_str = "[" + ", ".join(f"{c.name} ({c.cost})" for c in engine.hand) + "]"
print(f"Hand: {hand_str}")
print()

turn_result = engine.simulate_turn()
print("Turn execution:")
print(f"Strategy: {turn_result['Strategy']}")
print(f"Actions: {turn_result['Actions']}")

print()

report = engine.get_engine_status()
print(f"Game Report: {report}")

print()
print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
