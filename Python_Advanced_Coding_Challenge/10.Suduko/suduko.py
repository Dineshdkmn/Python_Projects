def is_valid(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # If there is no empty location, puzzle is solved
    if row == -1 and col == -1:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack

    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku Solved:")
    print_board(board)
else:
    print("No solution exists.")
