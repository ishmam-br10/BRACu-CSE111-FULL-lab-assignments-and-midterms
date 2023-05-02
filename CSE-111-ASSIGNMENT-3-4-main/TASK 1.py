# task 1
class Patient:
    def __init__(self, name , age, wi, hei):
        self.name = name
        self.age = age
        self.weight = wi
        self.height =hei
        self.BMI = (self.weight) / ((self.height/100) ** 2)
    def printDetails(self):
        print(f"Name: {self.name} \nAge: {self.age} \nWeight: {self.weight} \nHeight: {self.height} \nBMI: {self.BMI}")


# driver code
p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
