list_A = [False, False, True, True]
list_B = [False, True, False, True]

# Print the header of the truth table
print("Truth table - Booleans")
print("------------------------------")

#Print the header for the AND segment
print("AND")
print("------------------------------")
pos_AND = 0
while pos_AND != 4:
    # Retrieve the boolean from the lists based on our current position
    Selected_A = list_A[pos_AND]
    Selected_B = list_B[pos_AND]

    # Preform an if else with and to see the result
    result = False
    if Selected_A and Selected_B:
        result = True

    # Print the row
    print(f"{Selected_A} + {Selected_B} = {result}")
    # Move the position
    pos_AND += 1

# Print the end of the segment
print("------------------------------")

# Print the header for the OR segment
print("OR")
print("------------------------------")
pos_OR = 0
while pos_OR != 4:
    # Retrieve the boolean from the lists based on our current position
    Selected_A = list_A[pos_OR]
    Selected_B = list_B[pos_OR]

    # Preform an if else with and to see the result
    result = False
    if Selected_A or Selected_B:
        result = True
    # Print the row
    print(f"{Selected_A} + {Selected_B} = {result}")
    # Move the position
    pos_OR += 1

# Print the end of the segment
print("------------------------------")