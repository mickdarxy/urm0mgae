def generate_board():
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9:
                row.append("[ ]")
            else:
                row.append("   ")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print("".join(row))
        