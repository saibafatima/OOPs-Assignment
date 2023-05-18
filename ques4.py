# Q4. Why self is used in OOPs?

use_self_loop = "here the self keyword is used as a convention to refer to the instance(object) of a class within the class's methods ."

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person = Person("Alice", 25)

# Calling the introduce() method on the object
person.introduce()  # Output: Hello, my name is Alice and I am 25 years old.
