#create a function to calculate the fare with distance as parameters
def calculated_fare(distance):
     meters = distance * 1000 #valua that stores the kilometers to meters calculation
     #storing the rest of the calculations
     base_fare = 4.00
     time_spent = meters / 140
     #if statement to round up the time spent in meters
     if time_spent > round(time_spent, 0):
          time_spent = round(time_spent, 0) + 1


     meter_fare = time_spent * 0.25
     total_fare = base_fare + meter_fare
     return total_fare


input_distance = input("Distance Travelled: ")
print(f"Total fare: {round(calculated_fare(float(input_distance)), 2)} EUR")

