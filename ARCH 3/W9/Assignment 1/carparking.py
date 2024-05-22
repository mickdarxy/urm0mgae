from datetime import datetime
from math import ceil


class ParkedCar:
    def __init__(self, license_plate: str, check_in: datetime):
        self.license_plate = license_plate
        self.check_in = check_in if check_in else datetime.now()


class CarParkingMachine:

    def __init__(self, capacity = 10, hourly_rate = 2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate: str, check_in = None):
        # receive licenseplate as str
        #checkin as datetime object
        #if max capacity is reached it should return false w no more check ins
        if len(self.parked_cars) <= self.capacity:
            car = ParkedCar(license_plate, datetime.now())
            self.parked_cars.update({license_plate: car})
            return True
        return False

    def get_parking_fee(self, license_plate: str) -> float | None:
        if license_plate not in self.parked_cars:
            return None
        else:
            parking_time = datetime.now() - self.parked_cars[license_plate].check_in
            parking_hours = ceil(parking_time.total_seconds() / 3600)
            fee = round(min(parking_hours, 24) * self.hourly_rate, 2)
            print(fee)
            return round(fee)

    def check_out(self, license_plate: str):
        #return get_parking_fee total fee
        parking_fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)
        return parking_fee

def main():
    machine = CarParkingMachine( capacity=10, hourly_rate= 2.5)

    while True:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        option = input("Choose an option: ").upper()

        if option == 'I' or option == 'i':
            license_plate = input("Enter license plate: ")
            if machine.check_in(license_plate):
                print("License plate registered successfully\n Parking active")
        elif option == 'O' or option == 'o':
            license_plate = input("Enter license plate: ")
            parking_fee = machine.check_out(license_plate)
            if parking_fee:
                print(f"License plate recognized\n Open Fee: {parking_fee}")
        elif option == 'Q' or option == 'q':
            break


if __name__ == "__main__":
    main()




