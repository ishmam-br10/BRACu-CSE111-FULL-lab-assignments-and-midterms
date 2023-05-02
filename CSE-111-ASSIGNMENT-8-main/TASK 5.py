class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

## WRITE CODE FROM HERE
class ScienceExam(Exam):
    def __init__(self, mark, time, *sub):
        super().__init__(mark)
        self.time = time
        self.subject = sub
    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.subject) + 2}"
    def examSyllabus(self):
        subjectm = ' ,'.join(self.subject)
        return f"{super().examSyllabus()} ,{subjectm}"

    def examParts(self):
        a = super().examParts()
        for i in range(len(self.subject)):
            a += f"Part {i + 3}-{self.subject[i]}\n"
        return a

engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())