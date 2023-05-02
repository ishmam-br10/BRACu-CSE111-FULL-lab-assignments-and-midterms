class Student:
    ID = 0
    def __init__(self, name, dept, age, cgpa):
        Student.ID += 1
        self.name = name
        self.dept = dept
        self.age = age
        self.cgpa = cgpa
        self.ID = Student.ID
    @classmethod
    def from_String(cls, detail):
        list = detail.split("-")
        new = Student(list[0], list[1], list[2], list[3])
        return new

    def showDetails(self):
        print(f"ID: {self.ID}\nName: {self.name}\nDepartment: {self.dept}\nAge: {self.age}\nCGPA:{self.cgpa}")

# DRIVER
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

# sub task
print("class variable is a variable of the class that can be accessed from every method instance variable"
      "is a variable defined under a constructor or a method")
print(("Class method is a method defined in the class and can be accessed from anywhere and instance"
       "method does not take any parameter"))