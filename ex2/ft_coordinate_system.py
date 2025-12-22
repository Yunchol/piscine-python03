import math


def create_position(x, y, z):
    return (x, y, z)


def distance_3d(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def parse_coordinates(coord_str):
    parts = coord_str.split(",")
    if len(parts) != 3:
        raise ValueError("Invalid coordinate format")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    # 位置作成
    position = create_position(10, 20, 5)
    print(f"Position created: {position}")

    origin = (0, 0, 0)
    dist = distance_3d(origin, position)
    print(f"Distance between {origin} and {position}: {dist:.2f}")

    # 正常なパース
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parsed_pos = parse_coordinates(coord_str)
        print(f"Parsed position: {parsed_pos}")
        dist2 = distance_3d(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {dist2}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    # 不正なパース
    bad_coord_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_coord_str}"')
    try:
        parse_coordinates(bad_coord_str)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    # タプルのアンパック
    print("Unpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
