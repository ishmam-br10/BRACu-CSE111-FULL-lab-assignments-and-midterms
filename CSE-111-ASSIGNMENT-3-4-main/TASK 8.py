#TASK 8
class Student:
    def __init__(self, name, id, dept= 'CSE'):
        self.name = name
        self.id = id
        self.department = dept

    def dailyEffort(self, hours):
        self.effort = hours

    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.department}\nDaily Effort: {self.effort}hour(s)")
        if (self.effort) <= 2:
            print('Suggestion: Should give more effort!')
        elif self.effort <= 4:
            print('Suggestion: Keep up the good work!')
        else:
            print('Suggestion: Excellent! Now motivate others.')
# DRIVER CODE
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
