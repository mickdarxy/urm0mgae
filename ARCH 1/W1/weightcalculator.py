#weightcalculator

#define weight widgets and gizmos
#to assign a worth use def_ and what thing want to give a worth
def_widget = 75
def_gizmo = 112
 
 #input
 #int for a full number
 #input aka request an amount from the user
input_widgets = int(input("Number of widgets: "))
input_gizmos = int(input("Number of gizmos: "))
 
 #processing calculation
calc_widgets = def_widget * input_widgets
calc_gizmos = def_gizmo * input_gizmos
calc_total = calc_widgets + calc_gizmos
 
 #print the output 
print("The Total Weight Of The Order: " + str(calc_total) + " grams")