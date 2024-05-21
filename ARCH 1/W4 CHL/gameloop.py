#game loop
#loop while nested
#player game loop is finished when the game is finished
#player wins game ends
#waarde ontwikkelen voor winnende score
#wanneer wint of verliest een speler
#board game skeleton goed implementeren
#eerst main game loop maken en 
#goed lists doornemen 
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

board = generate_board()

print_board(board) 
    #final score: player whatever wins

    #alles hierin word de mainloop

def main(): #intro aanroepen etc
    GameRunning = True

    #player1
    #score
    #player2
    #score

    #create a board w a list and have each square give a certain value, if the player is on it etc
    #list = ["[X]",  ,  ,  ]
    
    while GameRunning :

        #check which player is going 
        #player one rolls the dice to determine which square it lands on
        #the player moves to the determined square
        #value of the square will be run through player which event?
        #does the player win or lose or buy or deny event
        #score checkboard
        #turn switches

        
        pass
    

    #alles hierin word de mainloop
if __name__ == str("__main__"):
    main()

