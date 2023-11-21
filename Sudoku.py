def solve_sudoku(grid):
                                                           # recursive depth-first search algorithm
    empty_cell = find_empty_cell(grid)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None  

def is_valid_move(grid, row, col, num):
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False
                                                                                       # current number is valid in the 3x3 subgrid
    subgrid_row_start, subgrid_col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row_start, subgrid_row_start + 3):
        for j in range(subgrid_col_start, subgrid_col_start + 3):
            if grid[i][j] == num:
                return False

    return True

def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    sudoku_grid = [
        [0, 3, 0, 6, 7, 0, 0, 0, 2],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 9, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_grid):
        print("SUDOKU SOLVED")
        print_sudoku(sudoku_grid)
    else:
        print(" NO SOLUTION EXISTS FOR THE GIVEN SUDOKU PUZZLE")
