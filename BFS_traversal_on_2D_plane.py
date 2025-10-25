import random
from collections import deque

# Directions: (dx, dy) and their movement names
directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

def is_valid(x, y, N, grid, visited):
    return 0 <= x < N and 0 <= y < N and grid[x][y] == 0 and not visited[x][y]

def bfs_traversal(grid, N, start, goal):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    queue.append((start[0], start[1], []))
    visited[start[0]][start[1]] = True

    while queue:
        x, y, path = queue.popleft()

        # Goal reached
        if (x, y) == goal:
            print("\nGoal Reached!")
            print("\nTraversal Path:")
            for step in path:
                print(step)
            return

        # Explore 4 directions
        for dx, dy, move in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, N, grid, visited):
                visited[new_x][new_y] = True
                step_info = f"Moving {move} -> ({new_x}, {new_y})"
                queue.append((new_x, new_y, path + [step_info]))

    print("No path found to the goal!")

# -------------------------------
# Main Program
# -------------------------------
def main():
    N = int(input("Enter grid size (N): "))

    # Generate random grid (0 = free, 1 = obstacle)
    grid = [[1 if random.randint(0, 3) == 0 else 0 for _ in range(N)] for _ in range(N)]

    print("\nGenerated Grid (0 = free, 1 = obstacle):")
    for row in grid:
        print(" ".join(map(str, row)))

    # User input for start and goal
    start = tuple(map(int, input("\nEnter Start position (row col): ").split()))
    goal = tuple(map(int, input("Enter Goal position (row col): ").split()))

    # Check for blocked cells
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        print("Start or Goal position is blocked by an obstacle!")
        return

    bfs_traversal(grid, N, start, goal)

# Run program
if __name__ == "__main__":
    main()
