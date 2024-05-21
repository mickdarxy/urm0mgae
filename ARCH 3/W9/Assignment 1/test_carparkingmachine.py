
import unittest
from datetime import datetime, timedelta
from carparking import CarParkingMachine

class SimpleCarParkingMachineTest(unittest.TestCase):
    def setUp(self):
        self.machine = CarParkingMachine(capacity=10, hourly_rate=2.5)
        self.license_plate = 'ABC123'
        self.machine.check_in(self.license_plate)

    def test_check_in(self):
        # Test that a car can be checked in
        result = self.machine.check_in('XYZ789')
        self.assertTrue(result, "Car should be checked in successfully")

    def test_get_parking_fee(self):
        # Test that the parking fee is calculated correctly
        # Assuming the car has been parked for 1 hour
        self.machine.parked_cars[self.license_plate].check_in = datetime.now() - timedelta(hours=1)
        fee = self.machine.get_parking_fee(self.license_plate)
        self.assertEqual(fee, 2.5, "Parking fee should be 2.5 for 1 hour")

    def test_check_out(self):
        # Test that checking out removes the car and returns the fee
        fee = self.machine.check_out(self.license_plate)
        self.assertIsNotNone(fee, "Fee should not be None after checkout")
        self.assertNotIn(self.license_plate, self.machine.parked_cars, "Car should be removed after checkout")

if __name__ == '__main__':
    unittest.main()
