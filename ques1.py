# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

class_ = "a class is a blueprint or template that defines the structure and behavior of objects"

object_ = "object represents a specific entity or item created from the class blueprint"

class Car:
    def __init__(self, brand , model, year):
        self.brand = brand
        self.model = model
        self.year = year 

    def accelerate(self):
        print("the car is accelerating.")
    
    def brake(self):
        print("the car is breaking.")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2021)

print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Mustang

car1.accelerate()  # Output: The car is accelerating.
car2.brake()      # Output: The car is braking.