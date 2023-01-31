class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_description(self):
        description = self.brand +" " + self.model + " of " + str(self.year)
        return description.title()
    def amount_of_fuel(self, fuel):
        self.fuel = fuel
        print("this car has "+ str(fuel) +"litres of fuel")
class Battery():
    def __init__(self, battery_capacity=50):
        self.battery_capacity = battery_capacity
    def range(self):
        if self.battery_capacity <= 50:
            range = 150
        else:
            range = 200
        print("this car can go on a range of " + str(range))
    def battery_size(self):
        if self.battery_capacity>=85:
            print("everything is fine")
        else:
            self.battery_capacity=85
            print("it's ready")
        return self.battery_capacity

class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery_capacity = Battery()
    def amount_of_fuel(self):
        print("electric car uses electricity")
audi = Car("audi", "a8", 2018)
print(audi.get_description())
audi.amount_of_fuel(10)
tesla = ElectricCar("tesla", "model 1", 2020)
print(tesla.get_description())
tesla.amount_of_fuel()
tesla.battery_capacity.range()
tesla.battery_capacity.battery_size()
tesla.battery_capacity.range()