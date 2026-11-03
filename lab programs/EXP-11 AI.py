# Map Coloring using CSP

colors = ["Red", "Green", "Blue"]

map = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

result = {}

def is_safe(region, color):
    for neighbor in map[region]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            result[region] = color

            if solve(regions[1:]):
                return True

            del result[region]

    return False

if solve(list(map.keys())):
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution found")
