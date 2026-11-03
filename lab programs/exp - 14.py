# Alpha-Beta Pruning

def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 2:
        return node

    if is_max:
        best = -999

        for child in node:
            value = alphabeta(
                depth + 1, child, alpha, beta, False
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for child in node:
            value = alphabeta(
                depth + 1, child, alpha, beta, True
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

tree = [[3, 5], [2, 9]]

result = alphabeta(0, tree, -999, 999, True)

print("Best value:", result)
