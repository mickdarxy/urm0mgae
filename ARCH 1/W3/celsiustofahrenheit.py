current_row = 0 
current_celsius = 0

print("-------")
print("°C °F ")

while current_celsius != 110:
    str_row = ""
    calc_fahrenheit = int((current_celsius * 1.8) + 32)

    str_row += str(current_celsius)

    if(len(str(current_celsius))) == 1:
        str_row += "   "
    elif (len(str(current_celsius))) == 2:
        str_row += "  "
    else: 
        str_row += " "

    str_row += str(calc_fahrenheit)

    print(str_row)

    current_celsius += 10
    str_row = ""

print("-------")
