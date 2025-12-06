def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        # Print board
        for r in board:
            print(r)
        print()
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # backtrack
    return res

if __name__ == "__main__":
    n = 4
    board = [[0]*n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")
