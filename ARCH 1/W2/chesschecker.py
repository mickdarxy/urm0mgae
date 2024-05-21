# Define a list of valid Letter positions
def_chessboard_letter_pos = ["a", "b", "c", "d", "e", "f", "g", "h"]

# request an input from the user
input_chessposition = input("Position: ")

# Retrieve the first and second part from the position
input_pos_p1 = input_chessposition[0]
input_pos_p2 = input_chessposition[1]

# Define the starting positions
selected_letter_pos_int = 0
next_pos = 0

# Loop over the chessboard letter position definition we made and if i match has been found then save that
# number to which the letter position is linked
for i in def_chessboard_letter_pos:
    if input_pos_p1.lower() == i:
        selected_letter_pos_int = next_pos
    else:
        next_pos = next_pos + 1

#Calculate the position
calc_position = selected_letter_pos_int + int(input_pos_p2) + 1

# After getting the letter position translated into a number, preform a modular arithmetic calculation
# and output the color of the position
if calc_position % 2:
    print("White")
else:
    print("Black")