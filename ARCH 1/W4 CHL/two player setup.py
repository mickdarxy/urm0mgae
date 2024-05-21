#two player setup
GameRunning = True
P1turn = True
P2turn = False
while GameRunning:
    #player 1 turn
    while P1turn:
        input("Player 1 Turn!\n")
        P1turn = False
        P2turn = True

    #player 2 turn
    while P2turn:
        input("Player 2 Turn!\n")
        P2turn2turn = False
        P1turn = True