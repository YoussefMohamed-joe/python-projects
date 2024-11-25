def is_valid_sudoku(grid):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            if grid[i][j] != 0:
                if grid[i][j] in row:
                    return False
                row.add(grid[i][j])
            if grid[j][i] != 0:
                if grid[j][i] in col:
                    return False
                col.add(grid[j][i])
            boxValue = grid[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]
            if not boxValue == 0:
                if boxValue in box:
                    return False
                box.add(boxValue)

    return True

grid = [
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

print(is_valid_sudoku(grid))