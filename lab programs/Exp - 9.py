from itertools import permutations

# Distance between cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]

min_distance = float('inf')
best_route = []

# Try all possible routes
for route in permutations(cities[1:]):
    route = (0,) + route + (0,)

    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    if total < min_distance:
        min_distance = total
        best_route = route

print("Best Route:", best_route)
print("Minimum Distance:", min_distance)
