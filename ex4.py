class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"the {self.name} is age of {self.age}")
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def display(self):
        super().display()
        print(f"subject of the teacher is {self.subject}")
class headteacher(teacher):
    def __init__(self,name, age, subject,office_number):
        super().__init__(name,age,subject)
        self.office_number = office_number
    def display(self):
        super().display()
        print(f"the office number of the teacher is {self.office_number}")

person1 = person("Ravi", 30)
teacher1 = teacher("Meena", 35, "Mathematics")
headteacher1 = headteacher("Anita", 45, "Science", "B-203")

print("Person Details:")
person1.display()
print("\nTeacher Details:")
teacher1.display()
print("\nHeadTeacher Details:")
headteacher1.display()
