import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        name = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = name.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        xyz: list[float] = []
        for part in parts:
            try:
                xyz = xyz + [float(part)]
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                break
        if len(xyz) == 3:
            return (xyz[0], xyz[1], xyz[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coord = get_player_pos()
    print(f"Got a first tuple: {coord}")
    print(f"It includes: X={coord[0]}, Y={coord[1]}, Z={coord[2]}")
    distance = math.sqrt(coord[0]**2 + coord[1]**2 + coord[2]**2)
    print(f"Distance to center: {round(distance, 4)}")
    print("Get a second set of coordinates")
    coord_second = get_player_pos()
    distance_second = math.sqrt(
        (coord_second[0] - coord[0])**2
        + (coord_second[1] - coord[1])**2
        + (coord_second[2] - coord[2])**2)
    print("Distance between the 2 sets of coordinates:"
          f" {round(distance_second, 4)}")


if __name__ == "__main__":
    main()
