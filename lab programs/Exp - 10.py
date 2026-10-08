import heapq

def a_star(graph, heuristic, start, goal):
    queue = [(0, start)]
    cost = {start: 0}
    path = {start: None}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            break

        for neighbour, distance in graph[current]:
            new_cost = cost[current] + distance

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                priority = new_cost + heuristic[neighbour]
                heapq.heappush(queue, (priority, neighbour))
                path[neighbour] = current

    # Create path
    result = []
    current = goal

    while current is not None:
        result.append(current)
        current = path[current]

    result.reverse()

    print("Path:", " -> ".join(result))
    print("Cost:", cost[goal])


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic values
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

a_star(graph, heuristic, 'A', 'D')
