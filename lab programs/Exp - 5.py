from collections import deque

def is_valid(m, c):
    # Number of people cannot be negative
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries should not be outnumbered
    if m > 0 and m < c:
        return False

    # On the other side
    m2 = 3 - m
    c2 = 3 - c

    if m2 > 0 and m2 < c2:
        return False

    return True


def solve():
    # State: (missionaries, cannibals, boat)
    # boat = 0 means left, 1 means right
    queue = deque([((3, 3, 0), [])])
    visited = {(3, 3, 0)}

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if (m, c) == (0, 0):
            return path + [state]

        for dm, dc in moves:
            if boat == 0:
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


solution = solve()

if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution")
