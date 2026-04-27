
# Base Class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} vehicle is moving.")

    def vehicle_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")

# The three subclasses
class Car(Vehicle):
    def move(self):
        print(f"{self.brand} car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} boat is sailing on water.")


# Function demonstrating polymorphism
def start_journey(vehicle):
    
    vehicle.vehicle_info()
    vehicle.move()
    print("\n")


# Main Program
car1 = Car("Toyota", 180)
plane1 = Plane("Boeing", 900)
boat1 = Boat("Yamaha", 120)

# List of different vehicle objects
vehicles = [car1, plane1, boat1]

# Process all objects uniformly
for vehicle in vehicles:
    start_journey(vehicle)