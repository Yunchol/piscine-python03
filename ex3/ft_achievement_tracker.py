def main():
    print("=== Achievement Tracker System ===")

    # 各プレイヤーの実績（setなので重複なし）
    alice = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }

    bob = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    # 全プレイヤーの実績を統合（union）
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    # 全員共通の実績（intersection）
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    # レア実績（1人しか持っていない）
    rare = set()
    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare.add(achievement)

    print(f"Rare achievements (1 player): {rare}")

    # Alice と Bob の比較
    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
