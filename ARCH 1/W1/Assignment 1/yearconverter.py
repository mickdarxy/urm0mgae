#pre define the variables
def_months = 12
def_days = 365

#input
Years = int(input("Years: "))

#processing
calc_months = def_months * Years
calc_days = def_days * Years

#output
print("Months: " + str(calc_months) + ", Days: " + str(calc_days))
