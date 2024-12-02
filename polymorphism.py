class Vehicle:  
    def move(self):  
        raise NotImplementedError("Subclasses must implement this method")  

class Car(Vehicle):  
    def move(self):  
        return "Driving 🚗"  

class Plane(Vehicle):  
    def move(self):  
        return "Flying ✈️"  

class Bicycle(Vehicle):  
    def move(self):  
        return "Pedaling 🚲"  

# Function to demonstrate polymorphism  
def show_vehicle_movement(vehicle):  
    print(vehicle.move())  

# Example of using the classes and polymorphism  
car = Car()  
plane = Plane()  
bicycle = Bicycle()  

show_vehicle_movement(car)      # Output: Driving 🚗  
show_vehicle_movement(plane)    # Output: Flying ✈️  
show_vehicle_movement(bicycle)  # Output: Pedaling 🚲