#create a function to check the triangles
def check_triangle(side_a, side_b, side_c):
#if loop to determine when its a possible or impossible triangle
#if side a is equal to side b and c
    if side_a >= side_b + side_c:
        return False # no triangle

    elif side_b >= side_a + side_c:
        return False

    elif side_c >= side_a + side_b:
        return False

    elif side_a == side_b == side_c:
        return True # True so possible triangle
    else:
        return True


side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

if check_triangle(side_a , side_b , side_c):
    print("Possible Triangle")
else:
    print("Impossible Triangle")