# Q5. What is inheritance? Give an example for each type of inheritance.

defi_ = "Inheritance is a fundamental concept in object-oriented programming (OOP) that allows the creation of new classes (derived classes) based on existing classes (base or parent classes)"

#single inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

# Creating an object of the derived class
dog = Dog()
dog.sound()  # Output: Dog barks.



#multiple inheritance
class Car:
    def drive(self):
        print("Car is being driven.")

class Boat:
    def sail(self):
        print("Boat is sailing.")

class AmphibiousVehicle(Car, Boat):
    pass

# Creating an object of the derived class
amphibious_vehicle = AmphibiousVehicle()
amphibious_vehicle.drive()  # Output: Car is being driven.
amphibious_vehicle.sail()   # Output: Boat is sailing.



#multilevel inheritance
class Vehicle:
    def accelerate(self):
        print("Vehicle is accelerating.")

class Car(Vehicle):
    def honk(self):
        print("Car is honking.")

class SportsCar(Car):
    def race(self):
        print("Sports car is racing.")

# Creating an object of the derived class
sports_car = SportsCar()
sports_car.accelerate()  # Output: Vehicle is accelerating.
sports_car.honk()       # Output: Car is honking.
sports_car.race()       # Output: Sports car is racing.




#hierarchial inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")

# Creating objects of the derived classes
dog = Dog()
cat = Cat()

dog.sound()  # Output: Dog barks.
cat.sound()  # Output: Cat meows.
