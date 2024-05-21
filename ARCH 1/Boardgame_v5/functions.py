# Import the required functions
import random
import questions
import colorama

# Define the collectors' items:
collectors_items = ["diamond", "emerald", "ruby", "sapphire", "amethyst", "opal", "moldavite", "rosequartz"]


def generate_board(players):
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9:
                row.append("[ ]")
            else:
                row.append("   ")
        board.append(row)

    # Locations of the questions
    # Trivia
    board[0][4] = f"[T]"
    board[3][9] = f"[T]"
    board[5][9] = f"[T]"
    board[9][7] = f"[T]"
    board[9][5] = f"[T]"
    board[9][0] = f"[T]"
    board[7][0] = f"[T]"

    # Guess the word
    board[0][3] = f"[W]"
    board[0][8] = f"[W]"
    board[7][9] = f"[W]"
    board[9][1] = f"[W]"
    board[4][0] = f"[W]"

    # Shops
    board[1][9] = f"[S]"
    board[8][0] = f"[S]"

    # Guess the number
    board[0][9] = f"[N]"
    board[9][9] = f"[N]"

    if players[0].x == players[1].x and players[0].y == players[1].y:
        board[players[0].y][players[0].x] = f"[{players[0].token}{players[1].token}]"
    else:
        for player in players:
            board[player.y][player.x] = f"[{player.token}]"

    return board


def move_player_location(curr_player):
    if curr_player.x < 9 and curr_player.y <= 8 and curr_player.direction == "right":
        curr_player.x += 1
        if curr_player.x == 9 and curr_player.y == 0:
            curr_player.direction = "down"
    elif curr_player.x == 9 and curr_player.y <= 8 and curr_player.direction == "down":
        curr_player.y += 1
        if curr_player.x == 9 and curr_player.y == 9:
            curr_player.direction = "left"
    elif curr_player.x >= 1 and curr_player.y == 9 and curr_player.direction == "left":
        curr_player.x -= 1
        if curr_player.x == 0 and curr_player.y == 9:
            curr_player.direction = "up"
    elif curr_player.x == 0 and curr_player.y >= 1 and curr_player.direction == "up":
        curr_player.y -= 1
        if curr_player.x == 0 and curr_player.y == 0:
            curr_player.direction = "right"


def print_board(board):
    for row in board:
        print("".join(row))


def roll_dice():
    die1 = random.randint(1, 6)
    return die1


def guess_the_word(curr_player):
    # Get the current players information
    current_playerinfo = curr_player.get_playerinfo()
    current_player_name = current_playerinfo[0]
    current_player_token = current_playerinfo[1]

    if current_player_name == "Player 1":
        print(f"Okay, {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. I hope you know your starsigns because we are going to guess one!")
    else:
        print(f"Okay, {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. I hope you know your starsigns because we are going to guess one!")

    words = questions.words

    # Select a random word
    selected_word_int = random.randint(0, len(words))
    selected_word = words[(selected_word_int - 1)]

    guess_count = 0
    guess_limit = 3
    guessed = False
    failed = False

    while guess_count != guess_limit:
        input_guess = input("Enter a guess: ")
        if input_guess.isalpha():
            if input_guess.lower() == selected_word:
                print(f"Congratulations!, You guessed the word {colorama.Fore.MAGENTA}{selected_word}{colorama.Style.RESET_ALL}!, You have been awarded {colorama.Fore.GREEN}2000{colorama.Style.RESET_ALL} money!")
                curr_player.add_money(2000)
                break
            elif (guess_count + 2) == guess_limit:
                print("You have one last change, Try again")
                guess_count += 1
            else:
                if (guess_count + 1) == guess_limit:
                    guess_count = guess_limit
                    break
                else:
                    print(f"Sorry wrong, Try again")
                    guess_count += 1

    if guess_count == guess_limit:
        print(f"Sorry, the word was {selected_word}, you lost {colorama.Fore.RED}1000{colorama.Style.RESET_ALL} money")
        curr_player.remove_money(1000)


def guess_the_number(curr_player):
    # Get the current player information
    current_playerinfo = curr_player.get_playerinfo()
    current_player_name = current_playerinfo[0]
    current_player_token = current_playerinfo[1]
    current_player_money = current_playerinfo[2]

    if current_player_name == "Player 1":
        print(f"Okay, {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. Its time to guess a number between 0 and 20")
    else:
        print(f"Okay, {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. Its time to guess a number between 0 and 20")

    guessed = False
    guess_attempts = 0
    chosen_number = random.randint(0, 20)
    while guess_attempts != 3 or not guessed:
        guess = input(f"Attempt {(guess_attempts + 1)}, What's your guess? : ")
        if guess.isnumeric():
            if int(guess) == chosen_number:
                print("You guessed the right number!, The number was " + str(chosen_number))
                print("You used " + str(guess_attempts) + " attempts!")

                selected_gem_int = random.randint(0, (len(collectors_items) - 1))
                selected_gem = collectors_items[selected_gem_int]

                print(f"You have been awarded the {colorama.Fore.GREEN}{selected_gem}{colorama.Style.RESET_ALL} gem!")
                curr_player.add_collected(selected_gem)
                guessed = True
            else:
                print("Sorry, wrong guess. Please try again")
                guess_attempts += 1
        else:
            print("Please guess a number!, This has cost you 1 attempt")
            guess_attempts += 1

        if guess_attempts == 3:
            guessed = True

    if guess_attempts == 3:
        print(f"You didn't guess the right number!, The number was {chosen_number}")
        if current_player_money < 500:
            curr_player.remove_money(current_player_money)
            print(f"You have lost {colorama.Fore.RED}all{colorama.Style.RESET_ALL} your money!")
        else:
            curr_player.remove_money(500)
            print(f"You have lost {colorama.Fore.RED}500{colorama.Style.RESET_ALL} money!")


def trivia(curr_player):
    current_playerinfo = curr_player.get_playerinfo()
    current_player_name = current_playerinfo[0]
    current_player_token = current_playerinfo[1]
    current_player_money = current_playerinfo[2]

    random_trivia_number = random.randint(0, 30)
    trivia_question = questions.questions[random_trivia_number]

    trivia_prompt = trivia_question.get_prompt()
    trivia_answer = trivia_question.get_answer()

    if current_player_name == "Player 1":
        print(f"{colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token} Its Trivia time!")
    else:
        print(f"{colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token} Its Trivia time!")

    print(f"Here is your question: {trivia_prompt}")
    input_user = input("Choice : ")
    if input_user.lower() == trivia_answer.lower():
        print(f"Correct!, the answer was {colorama.Fore.MAGENTA}{trivia_answer.upper()}{colorama.Style.RESET_ALL}, You have been awarded {colorama.Fore.GREEN}1000{colorama.Style.RESET_ALL} money")
        curr_player.add_money(1000)
    else:
        if current_player_money >= 500:
            print(f"Incorrect!, the answer was {colorama.Fore.MAGENTA}{trivia_answer.upper()}{colorama.Style.RESET_ALL}, You have lost {colorama.Fore.RED}500{colorama.Style.RESET_ALL} money")
            curr_player.remove_money(500)
        else:
            print(f"Incorrect!, the answer was {colorama.Fore.MAGENTA}{trivia_answer.upper()}{colorama.Style.RESET_ALL}, You have lost {colorama.Fore.RED}all{colorama.Style.RESET_ALL} your money")
            curr_player.remove_money(current_player_money)


def get_gem_list(curr_player):
    player_collected = curr_player.get_collected()

    diamond = 0
    emerald = 0
    ruby = 0
    sapphire = 0
    amethyst = 0
    opal = 0
    moldavite = 0
    rosequartz = 0
    unknown = 0

    for i in player_collected:
        if i == "diamond":
            diamond += 1
        elif i == "emerald":
            emerald += 1
        elif i == "ruby":
            ruby += 1
        elif i == "sapphire":
            sapphire += 1
        elif i == "amethyst":
            amethyst += 1
        elif i == "opal":
            opal += 1
        elif i == "moldavite":
            moldavite += 1
        elif i == "rosequartz":
            rosequartz += 1
        else:
            unknown += 1

    gem_list = [diamond, emerald, ruby, sapphire, amethyst, opal, moldavite, rosequartz]
    return gem_list


def get_gem_amount(curr_player, gem_selected):
    player_collected = curr_player.get_collected()
    gem_amount = 0
    for i in player_collected:
        if i == gem_selected:
            gem_amount += 1

    return gem_amount


def buy_gem(curr_player, curr_money, gem_selected):
    if curr_money >= 2000:
        curr_player.remove_money(2000)
        curr_player.add_collected(gem_selected)
        print(f"You have just bought '{gem_selected}' for {colorama.Fore.RED}2000{colorama.Style.RESET_ALL} money")
    else:
        print(f"{colorama.Fore.RED}You don't have enough money to buy this gem, try selling a gem if possible to get enough money.{colorama.Style.RESET_ALL}")


def sell_gem(curr_player, gem_selected):
    curr_gem_amount = get_gem_amount(curr_player, gem_selected)

    if curr_gem_amount >= 1:
        print(f"'{gem_selected}' SOLD for {colorama.Fore.GREEN}1000{colorama.Style.RESET_ALL}")
        curr_player.add_money(1000)
        curr_player.remove_collected(gem_selected)
    else:
        print(f"{colorama.Fore.RED}You don't have enough gems to sell{colorama.Style.RESET_ALL}")


def shop(curr_player):
    shopping = True
    while shopping:
        print("Buying/Selling options:")
        print("----------------------------------------------------------------------------")
        # Retrieve the list with the collectors' items and print the items under each other
        gem_collection_list = get_gem_list(curr_player)
        current_available_money = curr_player.get_money()
        gem_pos = 0
        for i in collectors_items:
            row = f"{i} - Buy price: 2000 - Sell price: 1000 - Owned currently: {gem_collection_list[gem_pos]}"
            print(row)
            gem_pos += 1
        print("----------------------------------------------------------------------------")
        print("To buy or sell please input which gem you want to select")
        print("Or to exit the shop, type 'exit'")
        # Create some spacing
        print("\n")
        print(f"Available money: {current_available_money}")

        # Check if a valid option was selected
        gem_selected = ""
        valid_option_selected = False
        while not valid_option_selected:
            input_option = input("Selected option : ")
            if input_option.isalpha():
                for e in collectors_items:
                    if input_option.lower() == e:
                        gem_selected = input_option
                        valid_option_selected = True

                if valid_option_selected:
                    pass
                elif input_option == "":
                    print("Invalid input, please enter a valid input")
                elif input_option.lower() == "exit":
                    gem_selected = "exit"
                    print("Leaving the shop")
                    shopping = False
                    valid_option_selected = True
                else:
                    print("Invalid input, please enter a valid input")
            else:
                print("Invalid input, please enter a valid input")

        if gem_selected != "exit":
            buyorsell = ""
            buyorsell_selected = False
            while not buyorsell_selected:
                input_option = input("Do you want to buy or sell? : ")
                if input_option.isalpha() and input_option.lower() == "buy":
                    buyorsell = "buy"
                    buyorsell_selected = True
                elif input_option.isalpha() and input_option.lower() == "sell":
                    buyorsell = "sell"
                    buyorsell_selected = True
                else:
                    print("Invalid input, please enter a valid input")

            if buyorsell == "buy" and gem_selected == "diamond":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "emerald":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "ruby":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "sapphire":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "amethyst":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "opal":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "moldavite":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "rosequartz":
                buy_gem(curr_player, current_available_money, gem_selected)
            elif buyorsell == "sell" and gem_selected == "diamond":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "emerald":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "ruby":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "sapphire":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "amethyst":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "opal":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "moldavite":
                sell_gem(curr_player, gem_selected)
            elif buyorsell == "sell" and gem_selected == "rosequartz":
                sell_gem(curr_player, gem_selected)
            else:
                pass


def change_player_location(player, dice_roll):
    for i in range(dice_roll):
        if player.direction == "Right":
            player.x = clip(player.x + 1, 0, 9)
            if player.x == 9:
                player.direction = "Down"
        elif player.direction == "Down":
            player.y = clip(player.y + 1, 0, 9)
            if player.y == 9:
                player.direction = "Left"
        elif player.direction == "Left":
            player.x = clip(player.x - 1, 0, 9)
            if player.x == 0:
                player.direction = "Up"
        elif player.direction == "Up":
            player.y = clip(player.y - 1, 0, 9)
            if player.y == 0:
                player.direction = "Right"


def clip(value, lower_bound, upper_bound):
    return min(max(value, lower_bound), upper_bound)
