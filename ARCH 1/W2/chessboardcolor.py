#chessboardcolor
def_letter_position = ["a", "b", "c", "d", "e", "f", "g", "h"]

#input
input_chesspiece_position = input("Position: ")

#make positions
input_position1 = input_chesspiece_position[0]
input_position2 = input_chesspiece_position[1]

#define positions
selected_letter_position_int = 0
next_position = 0 

#loop definition and combination
for i in def_letter_position:
    if input_position1.lower() == i:
        selected_letter_position_int = next_position
    else:
        next_position = next_position + 1 
     
#calculate the position   
calc_position = selected_letter_position_int = int(input_position2) + 1

#output
if calc_position % 2:
    print("White")
else: 
    print("Black")