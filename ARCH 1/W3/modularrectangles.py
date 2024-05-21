curr_row = 0
curr_celsius = 0

# Print the header of the table
print("-------")
print("°C  °F ")
# Make a loop that will stop when it reaches 110 degrees
# (Since we don't need to display it we can go up to there with our loop)
while curr_celsius != 110:
    str_row = ""
    # Convert the float calculation into an integer
    calc_fahrenheit = int((curr_celsius * 1.8) + 32)

    # Add the degrees in Celsius first to the table
    str_row += str(curr_celsius)

    # Check the length of the number and depending on the size add the needed amount of spaces
    if (len(str(curr_celsius))) == 1:
        str_row += "   "
    elif (len(str(curr_celsius))) == 2:
        str_row += "  "
    else:
        str_row += " "

    # Add the degrees in Fahrenheit as last to the string
    str_row += str(calc_fahrenheit)

    # Print the row
    print(str_row)

    # Add 10 extra degrees to the current Celsius and reset the row string
    curr_celsius += 10
    str_row = ""

# Finish the program of by printing the footer of the table
print("-------")

 