import random

#create a function to create options of arithmetic
def arithmetic_operation(arithmetic_type):
    result = 0 #empty variable of possible end result
    #here we have an if statement loop that groups each option
    if arithmetic_type.lower() == "summation":
        return summation()
    elif arithmetic_type.lower() == "multiplication":
        return multiplication()
    elif arithmetic_type.lower() == "subtraction":
        return subtraction()
    else:
        print("Invalid arithmetic. you can choose between summation, multiplication and subtraction")
        result = 404
        if result != 404:
            print(f"You had {result} correct and {(10 - result)} incorrect answers in \"{arithmetic_type}\"")

#create a function for the arithmetic group summation
def summation():
    result = 0 #empty value for the storage of result
    for i in range(10): #creates 10 arithmetic exercises
        figure1 = random.randint(1,100) #random digit 1-100
        figure2 = random.randint(1,100) #random digit 1-100
        fig_result = figure1 + figure2 #the answer is figure one and figure two in summation
        input_answer = input(f"{figure1} + {figure2} = ") #input created to allow the answer
        if input_answer.isnumeric() and int(input_answer) == fig_result:
            result += 1 #adds a point to the result counter if the answer given is correct
    return result

#function created for the multiplication of the arithmetics
def multiplication():
    result = 0 #result storage
    for i in range(10): #same routine used as above
        figure1 = random.randint(1, 100)
        figure2 = random.randint(1, 100)
        fig_result = figure1 * figure2 #here we have the used arithmetic as multiplication
        input_answer = input(f"{figure1} * {figure2} = ")
        if input_answer.isnumeric() and int(input_answer) == fig_result:
            result += 1
    return result


def subtraction():
    result = 0
    for i in range(10):
        figure1 = random.randint(1, 100)
        figure2 = random.randint(1, 100)
        fig_result = figure1 - figure2
        input_answer = input(f"{figure1} - {figure2} = ")
        if input_answer.isnumeric() and int(input_answer) == fig_result:
            result += 1
    return result


arithmetic_type = input("What type of arithmetic do you need to practice?: ")
arithmetic_operation(arithmetic_type)


