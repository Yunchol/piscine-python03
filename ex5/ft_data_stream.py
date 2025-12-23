def game_event_stream(count):
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 8, 12, 15]

    index = 0
    while index < count:
        player = players[index % len(players)]
        event = events[index % len(events)]
        level = levels[index % len(levels)]

        yield index + 1, player, level, event
        index += 1


def fibonacci_stream():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event_id, player, level, action in game_event_stream(total_events):
        processed += 1

        if processed <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) {action}")

        if level >= 10:
            high_level += 1

        if action == "found treasure":
            treasure_events += 1

        if action == "leveled up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: simulated")

    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=" ")
    fib = fibonacci_stream()
    for i in range(10):
        if i > 0:
            print(", ", end="")
        print(next(fib), end="")
    print()

    print("Prime numbers (first 5):", end=" ")
    primes = prime_stream()
    for i in range(5):
        if i > 0:
            print(", ", end="")
        print(next(primes), end="")
    print()
