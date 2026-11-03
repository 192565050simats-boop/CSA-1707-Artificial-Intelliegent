# Minimax Algorithm

def minimax(depth, node, is_max):
    if depth == 2:
        return node

    if is_max:
        return max(
            minimax(depth + 1, node[i], False)
            for i in range(2)
        )
    else:
        return min(
            minimax(depth + 1, node[i], True)
            for i in range(2)
        )

tree = [[3, 5], [2, 9]]

result = minimax(0, tree, True)

print("Best value:", result)
