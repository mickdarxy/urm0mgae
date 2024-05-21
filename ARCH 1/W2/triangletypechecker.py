#triangle type checker
#display input for the sides of the triangle
print("input lengths of each side of the triangle: ")

#request input of each side a b and c
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

#process all the operations
if a == b == c: 
    print("Equiliteral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
()