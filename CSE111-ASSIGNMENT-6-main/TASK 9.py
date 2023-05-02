#TASK 9
class Student:
    total = 0
    bracu = 0
    other = 0
    def __init__(self, name, department, institution  = 'BRAC University'):
        Student.total += 1
        self.name = name
        self.department = department
        self.institution = institution
        if self.institution == 'BRAC University':
            Student.bracu += 1
        else:
            Student.other += 1
    @classmethod
    def printDetails(cls):
        print(f'Total Student(s): {cls.total}')
        print(f'BRAC University Student(s): {cls.bracu}')
        print(f'Other Institution Student(s): {cls.other}')

    def individualDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.department}\nInstitution: {self.institution}")

    @classmethod
    def createStudent(cls, name, dept, ins= 'BRAC University'):
        new = cls(name, dept, ins)
        return new
#DRIVER CODE
Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
