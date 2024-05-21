current_position_width = 0
current_position_height = 0
str_row = ""

while current_position_height != 11:
    if current_position_height == 0:
        str_row += " "
        while current_position_width != 10:
            current_position_width += 1
            if current_position_width == 10:
                str_row += f"  {current_position_width}"
            else: 
                str_row += f"  {current_position_width}"

    else:
        str_row += f"{current_position_height}"
        while current_position_width != 10:
            calc_number = current_position_height * (current_position_width + 1)

            if len(str(calc_number)) == 1:
                str_row += f"   {calc_number}"
            else:
                str_row += f"  {calc_number}"

            current_position_width += 1
    print(str_row)
    str_row = ""
    current_position_height += 1
    current_position_width = 0
    

