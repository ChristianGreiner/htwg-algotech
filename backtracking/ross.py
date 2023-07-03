def is_valid_move(dx: int, dy: int):
    return abs(dx) + abs(dy) == 3 and abs(dx) < 3 and abs(dy) < 3

def in_bounds(x: int, y: int, n: int):
    return 0 <= x < n and 0 <= y < n

def ross(board, x, y, count):
    # Done!
    if count == len(board) * len(board[0]):
        return True

    for i in range(-2, 3):
        for j in range(-2, 3):
            next_x = x + i
            next_y = y + j

            if is_valid_move(i, j) and in_bounds(next_x, next_y, len(board)) and board[next_x][next_y] == 0:
                board[next_x][next_y] = count

                if ross(board, next_x, next_y, count + 1):
                    return True

                board[next_x][next_y] = 0

    return False

def print_board(board):
    print("----------------------------")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print("----------------------------")

if __name__ == "__main__":
    board_size = 5
    board = [[0] * board_size for _ in range(board_size)]
    ross(board, 0, 0, 0)
    print_board(board)


