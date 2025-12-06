def is_safe(graph, color, node, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m, color, node=0):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0  # backtrack
    return False

if __name__ == "__main__":
    # Example graph adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m = 3  # number of colors
    color = [0] * len(graph)

    if graph_coloring(graph, m, color):
        print("Solution exists: ", color)
    else:
        print("No solution exists")
