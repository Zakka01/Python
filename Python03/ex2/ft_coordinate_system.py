import math

def parse_coordinates(coors: str):
    try:
        a, b, c = coors.split(",")
        x, y, z = int(a), int(b), int(c)
        print(f"Parsing coordinates: \"{coors}\"")
        print(f"Parsed position: {x, y, z}")
        return (x, y, z)
    except ValueError as err:
        print(f"Parsing invalid coordinates: \"{coors}\"")
        print(f"Error parsing coordinates: {err}")
        print(f"Error details - Type: ValueError, Args: (\"{err}\",)")

def distance_formula(coors1: tuple, coors2: tuple):
    x1, y1, z1 = coors1
    x2, y2, z2 = coors2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {coors1} and {coors2}: {distance:.2f}")

def unpacking(coors: tuple):
    print(f"Player at x={coors[0]}, y={coors[1]}, z={coors[2]}")
    print(f"Coordinates: X={coors[0]}, Y={coors[1]}, Z={coors[2]}")

def coordinate_system():
    coordinates_one = tuple(0, 0, 0)
    coordinates_two = tuple(10, 20, 5)
    
    print(f"Position created: {coordinates_two}")
    distance_formula(coordinates_one, coordinates_two)
    
    print()
    parsed_coor = parse_coordinates("3,4,0")
    distance_formula(coordinates_one, parsed_coor)
    
    print()
    parsed_coor2 = parse_coordinates("abc,def,ghi")
    
    print()
    print("Unpacking demonstration:")
    unpacking(parsed_coor)
    

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    coordinate_system()
    