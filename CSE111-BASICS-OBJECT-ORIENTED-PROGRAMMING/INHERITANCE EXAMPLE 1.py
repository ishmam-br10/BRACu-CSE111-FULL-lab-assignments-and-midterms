class student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
    def do_class(self):
        print("Class done", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)
class cse_student(student):
    def do_lab(self):
        print("Lab done for student", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)

class eee_department(student):
    def do_lab(self):
        print("Lab done for student", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)

##################### command ##########
# st1 = student()
# st1.info("Peter Parker", 22301229, 4.00)
# st1.do_class()
# st2 = cse_student()
# st2.info("Peter Parker", 22301229, 4.00)
# st2.do_lab()
#s1 = student("Peter Parker", 22301229, 3.5)
c1 = cse_student("Peter Parker", 22301229, 3.6)
c1.do_lab()
class student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
    def do_class(self):
        print("Class done", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)
class cse_student(student):
    def do_lab(self):
        print("Lab done for student", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)

class eee_department(student):
    def do_lab(self):
        print("Lab done for student", "Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)

##################### command ##########
# st1 = student()
# st1.info("Peter Parker", 22301229, 4.00)
# st1.do_class()
# st2 = cse_student()
# st2.info("Peter Parker", 22301229, 4.00)
# st2.do_lab()
#s1 = student("Peter Parker", 22301229, 3.5)
c1 = cse_student("Peter Parker", 22301229, 3.6)
c1.do_lab()
