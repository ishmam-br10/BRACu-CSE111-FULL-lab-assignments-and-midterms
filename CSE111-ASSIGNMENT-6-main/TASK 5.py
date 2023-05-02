from datetime import date
class Employee:
    def __init__(self, name, year):
        self.name = name
        self.workingPeriod = year
    @classmethod
    def employeeByJoiningYear(cls, name, year1):
        exp = date.today().year - int(year1)
        new = Employee(name, exp)
        return new
    @staticmethod
    def experienceCheck(exper, gender):
        if gender == 'male' and exper< 3:
            return('He is not experienced')
        elif gender == 'male' and exper >= 3:
            return ("He is experienced")
        elif gender == 'female' and exper < 3:
            return ('She is not experienced')
        elif gender == 'female' and exper >= 3:
            return ("She is experienced")

# DRIVER CODE
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))