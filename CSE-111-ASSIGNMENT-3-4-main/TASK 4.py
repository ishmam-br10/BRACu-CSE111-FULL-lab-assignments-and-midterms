class Programmer:
    def __init__(self, name, lan, year):
        self.name = name
        self.language = lan
        self.year = year
        print("Horray a new programmer is born")
    def printDetails(self):
        print(f"Name : {self.name} \nLanguage: {self.language}\nExperience: {self.year}")
    def addExp(self, add):
        self.year= self.year + add
        print(f"Updating experience of {self.name}")
        # print(f"Name : {self.name} \nLanguage: {self.language}\nExperience: {self.year}")


# driver code
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()
