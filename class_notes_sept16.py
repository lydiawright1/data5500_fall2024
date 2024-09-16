class Car:
    def __init__(self, make, model, year, mileage, original_price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.original_price = original_price

    def calc_value(self, current_year):
        return self.original_price * (.90 ** (current_year - self.year))

andys_car = Car("Toyota", "Sequoia", 2014, 130000, 70000)

print(andys_car.calc_value(2024))

parkers_car = Car("Mazda", "3", 2014, 170000, 25000)

print(parkers_car.calc_value(2024))

katies_car = Car("Subaru", "Crosstrek", 2023, 16000, 25000)

print(katies_car.calc_value(2024))

corvette_car = Car("Chevrolet", "Corvette", 1967, 1000, 12000)

print(corvette_car.calc_value(2024))

class AntiqueCar(Car):
    #inherited constructor and calc_value from parent
    def calc_value(self, current_year):
        return self.original_price * (1.1 ** (current_year - self.year))

gregs_car = AntiqueCar("Cadillac", "Coupe De Ville", 1978, 50000, 10000)

print(gregs_car.calc_value(2024))

car_lot = [andys_car, parkers_car, katies_car, gregs_car]

total_car_lot_value = 0

for car in car_lot:
    total_car_lot_value += car.calc_value(2024)

print("total value: ", total_car_lot_value) 