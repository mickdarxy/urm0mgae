from datetime import datetime
from math import ceil


class ParkedCar:
    def __init__(self, license_plate: str, check_in: datetime):
        self.license_plate = license_plate
        self.check_in = check_in if check_in else datetime.now()


class CarParkingMachine:

    def __init__(self, id, capacity = 10, hourly_rate = 2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}
        self.id = id

        last_checkin = ""
        last_checkout = ""

        f = open("carparklog.txt", "r")
        for line in f:
            splitted_line = line.split(";")
            date_time = splitted_line[0]
            parking_machine = splitted_line[1].replace("cpm_name=", "")
            license_plate = splitted_line[2].replace("license_plate=", "")
            action = splitted_line[3].replace("action=", "").replace("\n", "")
            if action == "check-in":
                print(date_time)
                last_checkin = date_time
            else:
                last_checkout = date_time

        print(last_checkin)

        if last_checkin != "":
            if last_checkout != "":
                date_last_checkin = datetime.strptime(last_checkin, "%d-%m-%Y %H:%M:%S")
                date_last_checkout = datetime.strptime(last_checkout, "%d-%m-%Y %H:%M:%S")
                if date_last_checkin <= date_last_checkout:
                    pass
                else:
                    car = ParkedCar(license_plate, date_last_checkin)
                    self.parked_cars.update({license_plate: car})
            else:
                date_last_checkin = datetime.strptime(last_checkin, "%d-%m-%Y %H:%M:%S")
                car = ParkedCar(license_plate, date_last_checkin)
                self.parked_cars.update({license_plate: car})

        print(self.parked_cars)

    def check_in(self, license_plate: str, check_in = None):
        # receive licenseplate as str
        #checkin as datetime object
        #if max capacity is reached it should return false w no more check ins
        if len(self.parked_cars) <= self.capacity:
            car = ParkedCar(license_plate, datetime.now())
            self.parked_cars.update({license_plate: car})
            f = open("carparklog.txt", "a")
            f.write(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")};cpm_name={self.id};license_plate={license_plate};action=check-in\n")
            f.close()
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
        f = open("carparklog.txt", "a")
        f.write(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")};cpm_name={self.id};license_plate={license_plate};action=check-out;parking_fee={parking_fee}\n")
        f.close()
        return parking_fee


class CarParkingLogger:

    def __init__(self, id):
        self.id = id

    def get_machine_fee_by_day(self, car_parking_machine_id: str, search_date: str):
        if len(search_date) == 10 and search_date[2] == '-' and search_date[5] == '-':
            parking_fee_total = 0

            f = open("carparklog.txt", "r")
            for line in f:
                splitted_line = line.split(";")
                date_time = splitted_line[0]
                parking_machine = splitted_line[1].replace("cpm_name=", "")
                license_plate = splitted_line[2].replace("license_plate=", "")
                action = splitted_line[3].replace("action=", "")
                if parking_machine == car_parking_machine_id:
                    if action == "check-out":
                        parking_fee = int(splitted_line[4].replace("parking_fee=", ""))
                        date = date_time[0:10]
                        if date == search_date:
                            parking_fee_total += parking_fee

            return parking_fee_total
        else:
            return None

    def get_total_car_fee(self, license_plate: str):
        parking_fee_total = 0

        f = open("carparklog.txt", "r")
        for line in f:
            splitted_line = line.split(";")
            date_time = splitted_line[0]
            parking_machine = splitted_line[1].replace("cpm_name=", "")
            parking_license_plate = splitted_line[2].replace("license_plate=", "")
            action = splitted_line[3].replace("action=", "")
            if action == "check-out":
                parking_fee = int(splitted_line[4].replace("parking_fee=", ""))
                if license_plate == parking_license_plate:
                    parking_fee_total += parking_fee

        return parking_fee_total


def main():
    machine = CarParkingMachine(1, capacity=10, hourly_rate= 2.5)

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




