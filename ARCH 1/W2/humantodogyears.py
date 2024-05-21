#humantodogyears

def_output = ""

input_humanyears = float(input("Human Years: "))


if input_humanyears < 0:
    def_output = "only positive numbers are allowed"
else:
    calc_dogyears = 0

    if input_humanyears < 3:
       calc_dogyears =  input_humanyears * 10.5
    else: 
       input_humanyears = input_humanyears - 2
       calc_dogyears = (input_humanyears * 4) + 21
    
def_output = "Dog years: " + str(calc_dogyears)

print(def_output)