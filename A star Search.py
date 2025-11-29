from heapq import heappush, heappop

# Manhattan Distance Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search with battery constraint and consumption tracking
def a_star_search(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    # Battery equals Manhattan distance from start to goal
    battery = heuristic(start, goal)

    open_set = []
    heappush(open_set, (0, 0, start, battery))  # Track remaining battery

    came_from = {}
    g_score = {start: 0}
    battery_used = {start: 0}

    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    while open_set:

        f, g, current, remaining_battery = heappop(open_set)

        if current == goal:
            print(f"Battery remaining at goal: {remaining_battery}")
            print(f"Total battery used: {battery - remaining_battery}")
            return reconstruct_path(came_from, current)

        for dx, dy in moves:
            nx, ny = current[0] + dx, current[1] + dy

            if not (0 <= nx < rows and 0 <= ny < cols):
                continue

            if grid[nx][ny] == 1:
                continue

            neighbor = (nx, ny)
            tentative_g = g + 1
            battery_left = battery - tentative_g

            if battery_left < 0:
                continue

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                battery_used[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                came_from[neighbor] = current
                heappush(open_set, (f_score, tentative_g, neighbor, battery_left))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# -------------------------------
# RUN THE ALGORITHM
# -------------------------------
grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

start = (0, 0)
goal  = (4, 4)

path = a_star_search(grid, start, goal)

print("Shortest Path Found:")
print(path)
