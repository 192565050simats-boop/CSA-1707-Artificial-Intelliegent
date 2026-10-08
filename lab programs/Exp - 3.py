from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()

        print(jug1, jug2)

        if jug1 == target or jug2 == target:
            print("Target reached!")
            return

        states = [
            (capacity1, jug2),  # Fill Jug 1
            (jug1, capacity2),  # Fill Jug 2
            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2
            # Pour Jug 1 into Jug 2
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            # Pour Jug 2 into Jug 1
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution")

# Jug capacities: 4 litres and 3 litres
# Target: 2 litres
water_jug(4, 3, 2)
