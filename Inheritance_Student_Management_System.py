class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def display_info(self):
            print("Name:", self.name)
            print("Age:", self.age)

class Student(Person):
     def __init__(self, name, age, course):
          super().__init__(name, age)
          self.course= course
     def display_info(self):
          super().display_info()
          print("Course:", self.course)

class Lecturer(Person):
     def __init__(self, name, age, subject):
          super().__init__(name,age)
          self.subject= subject
     def display_info(self):
          super().display_info()
          print("Subject:", self.subject)

student1= Student("Joseph", 21, "Information Science")
lecturer1= Lecturer("Dr. Smith", 50, "Networking")

print("----Student----")
student1.display_info()

print("----Lecturer----")
lecturer1.display_info()





