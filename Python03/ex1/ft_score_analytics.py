import sys

def score_analytics():
    args = []
    if len(sys.argv) >= 2:
        try:
            for av in sys.argv[1:]:
                args.append(int(av))
            print(f"Scores processed: {args}")
            print(f"Total players: {len(args)}")
            print(f"Total score: {sum(args)}")
            print(f"Average score: {sum(args) / len(args)}")
            print(f"High score: {max(args)}")
            print(f"Low score: {min(args)}")
            print(f"Score range: {max(args) - min(args)}")
        except ValueError as e:
            print(f"Error: '{av}' is not a valid number")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()