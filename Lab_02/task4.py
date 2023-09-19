def calculate_knight_moves(knight):
    chessboard = [[0] * 8 for _ in range(8)]

    movements = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    x, y = knight

    for dx, dy in movements:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 8 and 0 <= new_y < 8:
            chessboard[new_x][new_y] = 3

    chessboard[x][y] = 33 

    return chessboard

knight = (3, 4)
board = calculate_knight_moves(knight)

for row in board:
    print(row)