class Player:
    def __init__(self, name: str):
        self.name = name
        self.achievements = set()
        
    def add_achievement(self, list_of_achievements: set):
        self.achievements = self.achievements.union(set(list_of_achievements))
        
def store_unique(players: set):
    uniques = set()
    for player in players:
        uniques = uniques.union(player.achievements)
    return uniques
    
def common_achievement(players: set):
    common = set()
    initial = True
    for p in players:
        if initial == True:
            common = p.achievements
            initial = False
        common = common.intersection(p.achievements)
    return common
    
def rare_achievement(players: set):
    rares = set()
    for p1 in players:
        others = set()
        for p2 in players:
            if p2 is not p1:
                others = others.union(p2.achievements)
        unique_to_p1 = p1.achievements.difference(others)
        rares = rares.union(unique_to_p1)
    return rares

def achievement_system():
    print("=== Achievement Tracker System ===\n")
    alice = Player("alice")
    bob = Player("bob")
    charlie = Player("charlie")

    alice.add_achievement({"first_kill", "level_10", "treasure_hunter", "speed_demon"})
    print(f"Player {alice.name} achievements: {alice.achievements}")
    
    bob.add_achievement({"first_kill", "level_10", "boss_slayer", "collector"})
    print(f"Player {bob.name} achievements: {bob.achievements}")
    
    charlie.add_achievement( {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"})
    print(f"Player {charlie.name} achievements: {charlie.achievements}")

    print()
    print("=== Achievement Analytics ===")
    players = {alice, bob, charlie}
    print(f"All unique achievements: {store_unique(players)} ")
    print(f"Total unique achievements: {len(store_unique(players))}")
    
    print()
    print(f"Common to all players: {common_achievement(players)}")
    print(f"Rare achievements (1 player): {rare_achievement(players)}")
    
    print()
    alice_bob = {alice, bob}
    print(f"Alice vs Bob common: {common_achievement(alice_bob)}")
    
    alice_unique = rare_achievement(alice_bob).difference(bob.achievements)
    print(f"Alice unique: {alice_unique}")
    
    bob_unique = rare_achievement(alice_bob).difference(alice.achievements)
    print(f"Bob unique: {bob_unique}")

if __name__ == "__main__":
    achievement_system()  
    