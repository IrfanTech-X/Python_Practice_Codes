from collections import deque

def bfs(grid,start,goal):
    N= len(grid)
    moves=[(1,0),(-1,0),(0,1),(0,-1)]
    q= deque([(start[0],start[1],0)])
    grid[start[0]][start[1]] = 0



    while q:
        x,y,level=q.popleft()
        if (x,y)==goal:
            return level
        

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<= nx< N and 0<= ny<N and grid[nx][ny]==1:
                grid[nx][ny]=0
                q.append((nx,ny,level+1))
    return -1
grid = [
    [0,0,1,0,1],
    [0,1,1,1,1],
    [0,1,0,0,1],
    [1,1,0,1,1],
    [1,0,0,0,1]
]
start =(0,2)
goal=(4,4)
steps =bfs(grid,start,goal)

if steps != -1:
    print("Goal found in", steps, "moves")
else:
    print("Goal is not found")