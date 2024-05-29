class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car, Vehicle):
    def __init__(self):
        self.price = 5000000
        self.vehicle_type = 'Personal car'

    def horse_powers(self):
        return 200


if __name__ == '__main__':
    nissan_car = Nissan()
    print(f"Vehicle type: {nissan_car.vehicle_type}")
    print(f"Price: {nissan_car.price}")
    print(f"Horse powers: {nissan_car.horse_powers()}")
