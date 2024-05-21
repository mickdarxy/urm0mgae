# Import the functions
import functions
import classes
import colorama
import time
import os

# Define the collectors items:
collectors_items = ["diamond", "emerald", "ruby", "sapphire", "amethyst", "opal", "moldavite", "rosequartz"]


def game():

    # Define the players
    player1 = classes.Player("Player 1", "🚀")
    player2 = classes.Player("Player 2", "🎩")
    players = [player1, player2]

    # Here we define a variable that will start as being initiated True
    # so that we can check if the game is running
    game_running = True

    # Here we have the main while-loop where the game will take place
    while game_running:
        for i in players:
            # Generate the board
            board = functions.generate_board(players)

            # Get the current player information
            current_playerinfo = i.get_playerinfo()
            current_player_name = current_playerinfo[0]
            current_player_token = current_playerinfo[1]
            current_player_money = current_playerinfo[2]
            current_player_position = current_playerinfo[3]
            current_player_properties = current_playerinfo[4]

            # Do a check to see if the player has collected all the gems
            collected_allgems = False
            player_gemlist = functions.get_gem_list(i)
            gemlist_diamond = player_gemlist[0]
            gemlist_emerald = player_gemlist[1]
            gemlist_ruby = player_gemlist[2]
            gemlist_sapphire = player_gemlist[3]
            gemlist_amethyst = player_gemlist[4]
            gemlist_opal = player_gemlist[5]
            gemlist_moldavite = player_gemlist[6]
            gemlist_rosequartz = player_gemlist[7]
            if gemlist_diamond >= 1 and gemlist_emerald >= 1 and gemlist_ruby >= 1 and gemlist_sapphire >= 1 and gemlist_amethyst >= 1 and gemlist_opal >= 1 and gemlist_moldavite >= 1 and gemlist_rosequartz >= 1:
                collected_allgems = True

            properties_str = ""
            for e in current_player_properties:
                if properties_str == "":
                    properties_str = e
                else:
                    properties_str += f", {e}"

            # Print the current players information
            if current_player_name == "Player 1":
                print(f"{colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token} - Money: {colorama.Fore.GREEN}{current_player_money}{colorama.Style.RESET_ALL} - Gems: {colorama.Fore.MAGENTA}{properties_str}{colorama.Style.RESET_ALL}\n\n")
            else:
                print(f"{colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token} - Money: {colorama.Fore.GREEN}{current_player_money}{colorama.Style.RESET_ALL} - Gems: {colorama.Fore.MAGENTA}{properties_str}{colorama.Style.RESET_ALL}\n\n")

            # Print the board each turn
            functions.print_board(board)

            # Create some spacing between the board and the player input
            print("\n")

            # Show the current player
            if current_player_name == "Player 1":
                print(f"current player: {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL}")
            else:
                print(f"current player: {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL}")

            if not collected_allgems:
                # Request an input from the player to throw the dice
                input_enter_pressed = input("Press enter to throw the dice")

                # Check if the player just pressed enter or typed anything else
                if input_enter_pressed != "":
                    print("Wrong input, just press enter please")
                else:
                    # Get the dice throw results
                    dice_result = functions.roll_dice()
                    print(f"You threw a dice, The result is: {colorama.Fore.CYAN}{dice_result}{colorama.Style.RESET_ALL}")

                    new_position = current_player_position + dice_result
                    if new_position >= 36:
                        new_position = 36 - new_position
                        print(f"You went round the board, You get {colorama.Fore.GREEN}500{colorama.Style.RESET_ALL} money")
                        i.add_money(500)

                    for m in range(dice_result):
                        functions.move_player_location(i)

                    i.new_position(new_position)

                    if new_position in [10, 30]:
                        functions.shop(i)
                    elif new_position in [4, 12, 14, 20, 22, 27, 29]:
                        functions.trivia(i)
                    elif new_position in [3, 8, 17, 26, 32]:
                        functions.guess_the_word(i)
                    elif new_position in [9, 18]:
                        functions.guess_the_number(i)
                    else:
                        pass
            else:
                # Print a victory message and close down the game
                # Show the current player
                if current_player_name == "Player 1":
                    print(f"{colorama.Fore.MAGENTA}Congratulations{colorama.Style.RESET_ALL}!, {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} you won the game!")
                else:
                    print(
                        f"{colorama.Fore.MAGENTA}Congratulations{colorama.Style.RESET_ALL}!, {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} you won the game!")

                game_running = False
                break

            time.sleep(1)
            os.system("cls")


game()
