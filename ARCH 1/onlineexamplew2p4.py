#online example
# Display a message prompting the user to input lengths of the sides of a triangle
print("Input lengths of the triangle sides: ")

# Request input from the user for the length of side 'x' and convert it to an integer
x = int(input("x: "))

# Request input from the user for the length of side 'y' and convert it to an integer
y = int(input("y: "))

# Request input from the user for the length of side 'z' and convert it to an integer
z = int(input("z: "))

# Check conditions to determine the type of triangle based on the lengths of its sides

# If all sides are equal, display that it's an equilateral triangle
if x == y == z:
    print("Equilateral triangle")
# If at least two sides are equal, display that it's an isosceles triangle
elif x == y or y == z or z == x:
    print("Isosceles triangle")
# If all sides have different lengths, display that it's a scalene triangle
else:
    print("Scalene triangle") 