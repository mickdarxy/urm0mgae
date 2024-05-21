List_A = [False, False, True, True]
List_B = [False, True, False, True]

print("-----------------------------")

print("AND")
print("-----------------------------")
position_AND = 0
while position_AND != 4:
    select_A = List_A[position_AND]
    select_B = List_B[position_AND]
    result = False
    if select_A and select_B:
        result = True

    print(f"{select_A}+{select_B} = {result}")
    position_AND += 1 
    
print("-----------------------------")

print("OR")
print("-----------------------------")
position_OR = 0
while position_OR != 4:
    select_A = List_A[position_OR]
    select_B = List_B[position_OR]
    result = False
    if select_A and select_B:
        result = True

    print(f"{select_A}+{select_B} = {result}")
    position_OR += 1
print("-----------------------------") 
 


