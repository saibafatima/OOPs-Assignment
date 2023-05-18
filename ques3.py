# Q3. Explain why the __init__() function is used. Give a suitable example.

use = "the init function is a special method in python classes that is automatically called when an object  of that class is created . the init functionis also known as constructor method."

class Person :
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"hello, my name is {self.name} and i am {self.age} years old.")

person1 = Person("alice ", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())