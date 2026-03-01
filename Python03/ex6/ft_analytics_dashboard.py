def list_management():
    players = ['alice', 'bob', 'charlie', 'diana']
    scores = [2300, 1800, 2150, 2050]
    active = [True, True, True, False]

    print("=== List Comprehension Examples ===")
    high_scorers = []
    for i in range(len(players)):
        if scores[i] > 2000:
            high_scorers.append(players[i])
    print(f"High scorers (>2000): {high_scorers}")


    scores_doubled = []
    for i in range(len(scores)):
        scores_doubled.append(scores[i] * 2)
    print(f"Scores doubled: {scores_doubled}")

    active_players = []
    for i in range(len(active)):
        if active[i] == True:
            active_players.append(players[i])
    print(f"Active players: {active_players}")
    
def dict_management():
    print("=== Dict Comprehension Examples ===")
    players = {"alice" : 2300, "bob" : 1800, "charlie" : 2150, "diana": 2050,  "eve": 1975,  "frank": 1080}
    categories = {"high": 0, "medium": 0, "low": 0}
    achievements = {"alice": 5, "bob": 3, "charlie": 7, "diana": 2,  "eve": 0,  "frank": 4}
    # get first 3 players
    print(f"Player scores: {dict(list(players.items())[:3])}")
    
    # update high, medium, low values depending on players score
    for value in players.values():
        if value < 1500:
            categories["low"] += 1
        elif 1500 <= value < 2000:
            categories["medium"] += 1
        else:
            categories["high"] += 1
    # print the categories
    print(f"Score categories: {categories}")
    # print achievements
    print(f"Achievement counts: {dict(list(achievements.items())[:3])}")

def set_management():
    print("=== Set Comprehension Examples ===")
    unique_players = {"alice", "bob", "charlie", "diana"}
    unique_achievement = {"first_kill", "level_10", "boss_slayer"}
    active_regions = {"north", "east", "central"}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievement}")
    print(f"Active regions: {active_regions}")

def analysis():
    print("=== Combined Analysis ===")
    players = ["alice", "bob", "charlie", "diana"]
    achievements = {'alice': 5, 'bob': 3, 'charlie': 7, 'diana': 2}
    all_unique_achievements = {'first_kill', 'level_10', 'boss_slayer', 'master_explorer', 'treasure_hunter',
        'event_champion', 'dungeon_cleared', 'puzzle_master', 'quick_draw', 'defender',
        'adventurer', 'team_player'}
    scores = [2300, 1800, 2150, 2050]
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(all_unique_achievements)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    
    top_score = max(scores) # Get top score 
    for i in range(len(scores)): # Get top score's index 
        if scores[i] == top_score:
            top_index = i
            break
    top_player = players[top_index]
    top_achievement = achievements[top_player]
    print(f"Top performer: {top_player} ({top_score} points, {top_achievement} achievements)")

def main():
    print("=== Game Analytics Dashboard ===\n")
    list_management()
    print()
    dict_management()
    print()
    set_management()
    print()
    analysis()

if __name__ == "__main__":
    main()