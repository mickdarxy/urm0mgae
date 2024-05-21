#pre define the variables
def_hours = 24
def_minutes = 1440
def_seconds = 86400

#input
input_days = int(input("Days: "))

#processing
calc_hours = input_days * def_hours
calc_minutes = def_minutes * input_days
calc_seconds = input_days * def_seconds

#print the result
print("Hours: " + str(calc_hours) + ", Minutes: " + str(calc_minutes) + ", Seconds: " + str(calc_seconds))