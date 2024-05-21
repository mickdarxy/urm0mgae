# Import the required functions
import random
import classes
import questions
import colorama

# Define the collectors items:
collectors_items = ["diamond", "emerald", "ruby", "sapphire", "amethyst", "opal", "moldavite", "rosequartz"]


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
    current_player_money = current_playerinfo[2]
    current_player_position = current_playerinfo[3]
    current_player_properties = current_playerinfo[4]

    if current_player_name == "Player 1":
        print(f"Okay, {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. I hope you know you're starsigns because we are going to guess one!")
    else:
        print(f"Okay, {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. I hope you know you're starsigns because we are going to guess one!")

    words = questions.words

    # Select a random word
    selected_word_int = random.randint(0, len(words))
    selected_word = words[selected_word_int]

    guess_count = 0
    guess_limit = 3
    guessed = False

    while guess_count != guess_limit and not guessed:
        input_guess = input("Enter a guess: ")
        if input_guess.isalpha():
            if input_guess == selected_word:
                guessed = True
                print(f"Congratulations!, You guessed the word {colorama.Fore.MAGENTA}{selected_word}{colorama.Style.RESET_ALL}!, You have been awarded {colorama.Fore.GREEN}2000{colorama.Style.RESET_ALL} money!")
                curr_player.add_money(2000)
            elif guess_count + 1 == guess_limit:
                print("You have one last chance, Try again")
                guess_count += 1
            else:
                print(f"Sorry wrong, Try again")
                guess_count += 1

    if guess_count == guess_limit:
        print(f"Sorry, the word was {selected_word}, you lost {colorama.Fore.RED}1000{colorama.Style.RESET_ALL} money")


def guess_the_number(curr_player):
    # Get the current player information
    current_playerinfo = curr_player.get_playerinfo()
    current_player_name = current_playerinfo[0]
    current_player_token = current_playerinfo[1]
    current_player_money = current_playerinfo[2]
    current_player_position = current_playerinfo[3]
    current_player_properties = current_playerinfo[4]

    if current_player_name == "Player 1":
        print(f"Okay, {colorama.Fore.RED}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. Its time to guess a number between 0 and 20")
    else:
        print(f"Okay, {colorama.Fore.BLUE}{current_player_name}{colorama.Style.RESET_ALL} {current_player_token}. Its time to guess a number between 0 and 20")

    guessed = False
    guess_attempts = 0
    chosen_number = random.randint(0, 20)
    while not guess_attempts < 3 or guessed:
        guess = input(f"Attempt {(guess_attempts + 1)}, What's your guess? : ")
        if guess.isnumeric():
            if int(guess) == chosen_number:
                print("You guessed the right number!, The number was " + str(chosen_number))
                print("You used " + str(guess_attempts) + " attempts!")

                selected_gem_int = random.randint(0, len(collectors_items))
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
        print(f"You didn't guess the right number!, The number was {chosen_number}")
        if current_player_money < 500:
            curr_player.remove_money(current_player_money)
            print(f"You have lost {colorama.Fore.RED}all{colorama.Style.RESET_ALL} your money!")
        else:
            curr_player.remove_money(500)
            print(f"You have lost {colorama.Fore.RED}500{colorama.Style.RESET_ALL} money!")


def initialize_board():
    # Create property instances (e.g., streets, utilities)
    properties = [
        classes.Property("Boardwalk", 400),
        classes.Property("Park Place", 350),
        classes.Property("TEST123", 350),
        # Add more properties...
    ]
    return properties

def trivia(curr_player):
    current_playerinfo = curr_player.get_playerinfo()
    current_player_name = current_playerinfo[0]
    current_player_token = current_playerinfo[1]
    current_player_money = current_playerinfo[2]
    current_player_position = current_playerinfo[3]
    current_player_properties = current_playerinfo[4]

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
    if input_user.lower == trivia_answer:
        print(f"Correct!, the answer was {colorama.Fore.MAGENTA}{trivia_answer.upper()}{colorama.Style.RESET_ALL}, You have been awarded {colorama.Fore.GREEN}1000{colorama.Style.RESET_ALL} money")
        curr_player.add_money()
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
        # Retrieve the list with the collectors items and print the items under each other
        gem_collection_list = get_gem_list(curr_player)
        current_avialable_money = curr_player.get_money()
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
        print(f"Available money: {current_avialable_money}")

        # Check if a valid option was selected
        gem_selected = ""
        valid_option_selected = False
        while not valid_option_selected:
            input_option = input("Selected option : ")
            if input_option.lower() == "exit":
                gem_selected = input_option.lower()
                valid_option_selected = True
            else:
                for e in collectors_items:
                    if input_option.lower() == e:
                        gem_selected = input_option
                        valid_option_selected = True

            if input_option.lower() == "exit":
                print("Leaving the shop")
                shopping = False
                valid_option_selected = True
                break
            elif gem_selected == "":
                print("Invalid input, please enter a valid input")
            elif valid_option_selected == True:
                pass
            else:
                print("Invalid input, please enter a valid input")

        if shopping:
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
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "emerald":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "ruby":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "sapphire":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "amethyst":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "opal":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "moldavite":
                buy_gem(curr_player, current_avialable_money, gem_selected)
            elif buyorsell == "buy" and gem_selected == "rosequartz":
                buy_gem(curr_player, current_avialable_money, gem_selected)
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
