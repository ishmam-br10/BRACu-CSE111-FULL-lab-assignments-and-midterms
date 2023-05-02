class student:
    uni_name = "BRACU"
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print('Name: ', self.name, "ID:", self.id, "University: ", student.uni_name)

    ## i am creating a instance method just to figure out the differences between the class and instance
    ## just comment out the section and vice versa if you get confused
    # def up_uni_name(self, up_name):
    #     self.uni_name = up_name

    @classmethod
    def up_uni_name(cls, up_name):
        cls.uni_name = up_name

############## command line ####################

s1 = student("Peter Parker", 99)
s2 = student("Michelle Jones", 98)
s1.details()
s2.details()
print(student.uni_name)
student.up_uni_name("BRAC University")
s1.details()
s2.details()
print(student.uni_name)
