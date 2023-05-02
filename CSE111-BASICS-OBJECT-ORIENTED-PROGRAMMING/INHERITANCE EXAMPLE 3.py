class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print("Name: ", self.name, "Id: ", self.id)

#===========================================================================

class cse_student(student):
    def __init__(self, name, id, labs):
        super().__init__(name, id)
        self.labs = labs
    def cry(self):
        print(f"Engineering student, {self.name} is crying because of  {self.labs} labs")


#============================================================================

class medical_student(student):
    def __init__(self, name, id):
        super().__init__(name, id)
    def party(self):
        print(f"Medical student {self.name} is doing all day party")

#============== Command line ====================

s1 = cse_student("Michelle Jones", 778, 3)
s2 = medical_student("Stephen Strange", 4841)
s1.cry()
s2.party()