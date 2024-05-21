#define variables
def_taxpercentage = 0.21
def_tipperpercentage = 0.15

#input
input_cost = float(input("Cost of the meal: "))

#processing
calc_tax = round((float(input_cost) * def_taxpercentage), 3)
calc_tip = round((float(input_cost) * def_tipperpercentage), 3)
calc_total = round((calc_tax + calc_tip + input_cost), 3)

#output 
print("Tax: " + str(calc_tax) + ", Tip: " + str(calc_tip) + ", Total: " + str(calc_total))
