# chapter_6.py

from vehicle import Vehicle, Car, Truck

my_car = Car("Ford", "Thunderbird")
print(f"my_car is type {type(my_car)}")
print(f"my_car uses {my_car.fuel}")

print(f"my_car is a Car: {isinstance(my_car, Car)}")
print(f"my_car is a Vehicle: {isinstance(my_car, Vehicle)}")
print(f"Car is a subclass of Vehicle: {issubclass(Car, Vehicle)}")

my_truck = Truck("Ford", "F350")
print(f"my_truck is type {type(my_truck)}")
print(f"my_truck uses {my_truck.fuel}")
print(f"my_truck has {my_truck.number_of_wheels} wheels")