def generate_board(players):
    # Get the player positions
    player1_pos = players[0].get_position()
    player2_pos = players[1].get_position()

    print(f"player1_pos : {player1_pos}")
    print(f"player2_pos : {player2_pos}")

    # Get the player tokens
    player1_token = players[0].get_token()
    player2_token = players[1].get_token()

    board = []
    for i in range(10):
        row = []
        position = 0
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9:
                 if player1_pos == position and player2_pos == position:
                     row.append(f"[{player1_token}{player2_token}]")
                 elif player1_pos == position:
                     row.append(f"[{player1_token}]")
                 elif player2_pos == position:
                     row.append(f"[{player2_token}]")
                 else:
                     row.append("[ ]")
                     position += 1
            else:
                row.append("   ")

            position += 1
        board.append(row)
    return board