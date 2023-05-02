class student:
    university_name = "BRAC University"  ## static variable beacuse it is accessible from all around the function
    student_number = 0
    def __init__(self, name, id, dept):
        self.name = name    #instance variable
        self.id = id        #instance variable
        self.dept = dept    #instance variable

        student.student_number = student.student_number + 1


#+++++++++++++++ command line

st1 = student("Tony stark", 22301229, "cse")
st2 = student("Natasha Romanoff", 22301225, "CS")

print(student.student_number)
print(st1.name)