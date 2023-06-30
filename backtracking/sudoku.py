# WIP
def find_empty_pos(arr):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                return row, col
    return -1, -1

def box_used(arr, col, row, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False

def col_used(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False

def row_used(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False

def is_valid_move(arr, row, col, num):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    return (
        not col_used(arr, col, num) and
        not row_used(arr, row, num) and
        not box_used(arr, start_row, start_col, num)
    )

def solver(sudoku):
    row, col = find_empty_pos(sudoku)

    if (row == -1 and col == -1):
        return True

    for num in range(1, 10):
        if (is_valid_move(sudoku, row, col, num)):
            sudoku[row][col] = num
            
            # Success
            succ, _ = solver(sudoku)
            if succ:
                return True
            
            # Failed
            sudoku[row][col] = 0

    return False

if __name__=="__main__":
    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    _, sudoku = solver(sudoku)
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = " ")
        print()