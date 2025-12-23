def main():
    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]
    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "level_20", "rare_item"],
        "bob": ["first_kill", "level_10", "level_20"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "speed_run", "rare_item", "legend", "master"],
        "diana": ["first_kill"],
    }
    active_players = ["alice", "bob", "charlie"]
    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }

    # =========================
    # List Comprehension
    # =========================
    print("\n=== List Comprehension Examples ===")

    high_scorers = [name for name, score in scores.items() if score > 2000]
    print("High scorers (>2000):", high_scorers)

    doubled_scores = [score * 2 for score in scores.values()]
    print("Scores doubled:", doubled_scores)

    active = [p for p in players if p in active_players]
    print("Active players:", active)

    # =========================
    # Dict Comprehension
    # =========================
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {name: score for name, score in scores.items()}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([s for s in scores.values() if s >= 2200]),
        "medium": len([s for s in scores.values() if 2000 <= s < 2200]),
        "low": len([s for s in scores.values() if s < 2000]),
    }
    print("Score categories:", score_categories)

    achievement_counts = {name: len(ach) for name, ach in achievements.items()}
    print("Achievement counts:", achievement_counts)

    # =========================
    # Set Comprehension
    # =========================
    print("\n=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    print("Unique players:", unique_players)

    unique_achievements = {a for ach_list in achievements.values() for a in ach_list}
    print("Unique achievements:", unique_achievements)

    active_regions = {regions[p] for p in active_players}
    print("Active regions:", active_regions)

    # =========================
    # Combined Analysis
    # =========================
    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    print("Total players:", total_players)

    total_unique_achievements = len(unique_achievements)
    print("Total unique achievements:", total_unique_achievements)

    average_score = sum(scores.values()) / len(scores)
    print("Average score:", average_score)

    top_player = max(scores, key=scores.get)
    print(
        "Top performer:",
        top_player,
        f"({scores[top_player]} points, {len(achievements[top_player])} achievements)",
    )


if __name__ == "__main__":
    main()
