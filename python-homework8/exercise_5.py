class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def describe(self):
        return f"{self.name} is in grade {self.grade}"

student1 = Student("nino", 10)
student2 = Student("giorgi", 11)

print(student1.describe())
print(student2.describe())