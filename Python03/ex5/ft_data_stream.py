import time

def game_data_stream(total_events: int):
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    for i in range(total_events):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = ((i * 7) % 12) + 5
        yield player, level, event
        
def fibonacci_formula():
    x, y= 0, 1
    while True:
        yield x
        x, y = y, x + y
        
def prime_formula():
    x = 2
    while x <= 11:
        y = 2
        is_prime = True
        while y < x:
            if x % y == 0:
                is_prime = False
                break
            y += 1
        if is_prime == True:
            yield x
        x+=1 

def main():
    print("=== Game Data Stream Processor ===\n")
    total_events = 1000
    print(f"Processing {total_events} game events...\n")
    stream = game_data_stream(total_events)
    
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    
    start = time.time() #time beefore the loop

    while 1:
        try:
            player, level, event = next(stream)
        except StopIteration:
            break

        total += 1
        
        # printing 3 first events
        if total <= 3:
            print(f"Event {total}: Player {player} (level {level}) {event}")
        elif total == 4:
            print("...\n")

        # counting event number on each
        if level >= 10:
            high_level += 1
        if "found treasure" in event:
            treasure += 1
        if "leveled up" in event:
            level_up += 1
        
    end = time.time() #time after the loop

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {(end - start):.3f} seconds")
    
    print("\n=== Generator Demonstration ===")
    
    fibo_numbers = []
    fibo = fibonacci_formula()
    for m in range(10):
        fibo_numbers.append(next(fibo))
        
    prime_num = []
    prime = prime_formula()
    for m in range(5):
        prime_num.append(next(prime))
    
    print("Fibonacci sequence (first 10):", *fibo_numbers , sep=", ")
    print("Prime numbers (first 5):", *prime_num, sep=", ")

if __name__ == "__main__":
    main()