#sides to shape converter
input_sides = int(input("Sides: "))

#processing with boolean
if input_sides < 3:
    print("incorrect value, this cannot be a shape")
elif input_sides == 3:
    print("triangle")
elif input_sides == 4:
    print("square")
elif input_sides == 5:
    print("pentagon")
elif input_sides == 6:
    print("hexagon")    
elif input_sides == 7:
    print("heptagon")
elif input_sides == 8:
    print("octagon")
elif input_sides == 9:
    print("nonagon")
elif input_sides == 10:
    print("decagon")
else: 
    print("cannot have more than 10 sides")