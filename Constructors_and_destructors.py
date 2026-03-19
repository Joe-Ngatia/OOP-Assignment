# Constructors_and_Deconstructors.py

class Person:
    def __init__(self, name="Unknown", age=0):
        # Check age is a positive integer
        if age < 0:
            raise ValueError("Age must be a positive number")
        self.name = name
        self.age = age

    # Alternative constructor from string "Name-Age"
    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    # Display object nicely
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    # Destructor message
    def __del__(self):
        print(f"{self.name} object destroyed")


# --- TESTS ---
print("Default constructor:")
p1 = Person()
print(p1)

print("\nParameterized constructor:")
p2 = Person("Alice", 30)
print(p2)

print("\nAlternative constructor:")
p3 = Person.from_string("Bob-25")
print(p3)

print("\nInput validation test:")
try:
    p4 = Person("Invalid", -5)
except ValueError as e:
    print("Error:", e)

# Delete an object to show destructor
del p2