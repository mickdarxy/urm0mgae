#two player game loop with scores and shit or main 

round_number = 0
player_list = ["Player 1", "PLayer 2"]
score_list = [0, 0]

while True:
    round_number += 1
    print("ROUND:", round_number)
    if round_number%2:
        print(player_list[1], "GETS TO PLAY")
        input("press a key:\n\n") #\n is a line space or enter
        score_list[0]+=1
        print("SCORES: \n", player_list[0],"\n", score_list[0],":", score_list[1]  )

    else:
        print(player_list[0], "GETS TO PLAY")
        input("press a key:\n\n")
        score_list[1]+=1
        print("SCORES:\n PLAYER 1:", score_list[0],"\n" )
