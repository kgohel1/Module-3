class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass Automobile
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

year = int(input("Enter the year of the car: "))
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
doors = input("Enter number of doors: ")
roof = input("Enter type of roof: ")

my_car = Automobile(year, make, model, doors, roof)


print("\nVehicle Details:")
print(f"Vehicle type: {my_car.vehicle_type}")
print(f"Year: {my_car.year}")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Number of doors: {my_car.doors}")
print(f"Roof type: {my_car.roof}")
