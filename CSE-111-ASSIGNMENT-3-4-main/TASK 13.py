# TASK 13
class StudentDatabase:
     def __init__(self, name, id):
         self.name = name
         self.id = id
         self.grades = {}
     def calculateGPA(self, grade_list, semester):
         self.grade_list = grade_list
         self.semester = semester

         cgpa = 0
         courses = []
         dictionary2 = {}
         for i in grade_list:
             list1 = i.split(':') # dividing the list on basis of : and making them
             courses.append(list1[0])
             cgpa = cgpa + float(list1[1])

         self.cgpa_final = cgpa / len(courses)
         dictionary2[tuple(courses)] = float(f'{self.cgpa_final:.2f}')
         dictionary3 = {}
         dictionary3[semester] = dictionary2
         self.grades.update(dictionary3)

     def printDetails(self):
         print(f'Name: {self.name}')
         print(f"ID: {self.id}")
         for key, value in self.grades.items():
             print(f"Courses taken in {key} :")
             for i,j in value.items():
                 for k in i:
                     print(k)

                 print(f"GPA: {j}")

# DRIVER CODE

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
