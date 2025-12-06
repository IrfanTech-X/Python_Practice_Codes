import random

nodes_visited = 0
nodes_pruned = 0

def generate_leaf_scores(num_leaves):
    return [random.randint(0, 100) for _ in range(num_leaves)]

def alpha_beta(tree, depth, index, maximizingPlayer, alpha, beta):
    global nodes_visited, nodes_pruned
    nodes_visited += 1

    # Base case: leaf node
    if depth == 0:
        return tree[index]

    # Maximizing player
    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(2):  # 2 children for binary tree
            val = alpha_beta(tree, depth - 1, index * 2 + i, False, alpha, beta)
            maxEval = max(maxEval, val)
            alpha = max(alpha, val)
            if beta <= alpha:  # Prune
                nodes_pruned += 1
                break
        return maxEval

    # Minimizing player
    else:
        minEval = float('inf')
        for i in range(2):
            val = alpha_beta(tree, depth - 1, index * 2 + i, True, alpha, beta)
            minEval = min(minEval, val)
            beta = min(beta, val)
            if beta <= alpha:  # Prune
                nodes_pruned += 1
                break
        return minEval


if __name__ == "__main__":
    num_leaves = 16
    depth = 4

    tree = generate_leaf_scores(num_leaves)
    print("Leaf scores:", tree)

    nodes_visited = 0
    nodes_pruned = 0

    optimal_value = alpha_beta(tree, depth, 0, True, float('-inf'), float('inf'))

    print("Optimal value:", optimal_value)
    print("Nodes visited:", nodes_visited)
    print("Nodes pruned:", nodes_pruned)
