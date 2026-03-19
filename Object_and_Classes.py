# Object_and_Classes.py
# This file demonstrates the concept of objects and classes in Python

# Define a class (blueprint)
class Student:
    def __init__(self, name, age):
        # Attributes (data)
        self.name = name
        self.age = age

    # Method (behavior)
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating objects (instances of the class)
student1 = Student("Joseph", 21)
student2 = Student("Brian", 22)

# Calling methods
student1.display()
student2.display()