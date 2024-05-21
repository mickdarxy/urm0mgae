def get_parking_fee(self, license_plate):
    parked_car = self.parked_cars.pop(license_plate, None)
    if parked_car:
        parking_duration = datetime.now() - parked_car.check_in
        parking_hours = parking_duration.total_seconds() // 3600
        parking_hours = min(parking_hours + 1, 24)  # Round up and max of 24 hours
        return round(parking_hours * self.hourly_rate, 2)
    return None

'''In this example, ceil from the math module is used to round up the number of hours. 
The min function ensures that the fee does not exceed the maximum daily rate (24 hours).
 The round function is used to ensure the fee is presented with two decimal places.
Remember to import the ceil function from the math module at the beginning of your script:
Python from math import ceil'''
from datetime import datetime, timedelta

def get_parking_fee(check_in, hourly_rate):
    # Calculate the total time parked in seconds
    parking_duration = datetime.now() - check_in
    # Convert the duration to hours and round up
    parking_hours = ceil(parking_duration.total_seconds() / 3600)
    # Calculate the fee (capped at 24 hours)
    fee = min(parking_hours, 24) * hourly_rate
    return round(fee, 2)  # Round the fee to 2 decimal places

# Example usage:
# Assuming the car checked in 3 hours and 15 minutes ago
check_in_time = datetime.now() - timedelta(hours=3, minutes=15)
hourly_rate = 2.50
fee = get_parking_fee(check_in_time, hourly_rate)
print(f"The parking fee is: {fee} EUR")

    def get_parking_fee(self, license_plate: str) -> float | None:
        if license_plate not in self.parked_cars:
            return None
        else:
            return min(math.ceil((datetime.now() - self.parked_cars[license_plate].check_in).total_seconds() / 3600), 24) * self.hourly_rate



    def get_parking_fee(self, license_plate: str) -> float | None:
        if license_plate not in self.parked_cars:
            return None
        else:
            parking_time = datetime.now() - check_in
            parking_hours = ceil(parking_time.total_seconds() / 3600)
            fee = min(parking_hours, 24) * hourly_rate
            return round(fee, 2)
