def print_inventory(player_name, inventory):
    print(f"=== {player_name}'s Inventory ===")

    total_value = 0
    total_items = 0
    categories = {}

    for item_name, info in inventory.items():
        qty = info.get("quantity")
        value = info.get("value")
        category = info.get("category")
        rarity = info.get("rarity")

        item_total = qty * value
        total_value += item_total
        total_items += qty

        categories[category] = categories.get(category, 0) + qty

        print(f"{item_name} ({category}, {rarity}): "
              f"{qty}x @ {value} gold each = {item_total} gold")

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    print("Categories:", end=" ")
    first = True
    for cat, count in categories.items():
        if not first:
            print(", ", end="")
        print(f"{cat}({count})", end="")
        first = False
    print()
    return total_value, total_items


def transfer_item(from_inv, to_inv, item, amount):
    if item not in from_inv:
        return False

    if from_inv[item].get("quantity") < amount:
        return False

    from_inv[item]["quantity"] -= amount

    if item in to_inv:
        to_inv[item]["quantity"] += amount
    else:
        to_inv[item] = from_inv[item].copy()
        to_inv[item]["quantity"] = amount

    return True


if __name__ == "__main__":
    print("=== Player Inventory System ===")

    players = {
        "Alice": {
            "sword": {
                "category": "weapon",
                "rarity": "rare",
                "quantity": 1,
                "value": 500
            },
            "potion": {
                "category": "consumable",
                "rarity": "common",
                "quantity": 5,
                "value": 50
            },
            "shield": {
                "category": "armor",
                "rarity": "uncommon",
                "quantity": 1,
                "value": 200
            }
        },
        "Bob": {
            "magic_ring": {
                "category": "accessory",
                "rarity": "rare",
                "quantity": 1,
                "value": 300
            }
        }
    }

    alice_value, alice_items = print_inventory("Alice", players["Alice"])

    print("=== Transaction: Alice gives Bob 2 potions ===")
    if transfer_item(players["Alice"], players["Bob"], "potion", 2):
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {players['Alice']['potion']['quantity']}")
    print(f"Bob potions: {players['Bob']['potion']['quantity']}")

    print("=== Inventory Analytics ===")

    max_value = 0
    max_value_player = ""
    max_items = 0
    max_items_player = ""
    rare_items = {}

    for name, inv in players.items():
        value, items = print_inventory(name, inv)

        if value > max_value:
            max_value = value
            max_value_player = name

        if items > max_items:
            max_items = items
            max_items_player = name

        for item_name, info in inv.items():
            if info.get("rarity") == "rare":
                rare_items[item_name] = True

    print(f"Most valuable player: {max_value_player} ({max_value} gold)")
    print(f"Most items: {max_items_player} ({max_items} items)")

    print("Rarest items:", end=" ")
    first = True
    for item in rare_items.keys():
        if not first:
            print(", ", end="")
        print(item, end="")
        first = False
    print()
