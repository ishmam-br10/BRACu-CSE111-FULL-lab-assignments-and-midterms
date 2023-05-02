#TASK 7
class Cat:
    Number_of_cats = 0
    def __init__(self, clr, ac):
        Cat.Number_of_cats += 1
        self.clr = clr
        self.ac = ac

    @classmethod
    def no_parameter(cls):
        new = Cat('White', 'sitting')
        return new
    @classmethod
    def first_parameter(cls, clr):
        new = Cat(clr, 'sitting')
        return new
    @classmethod
    def second_parameter(cls, ac):
        new = Cat('Grey', ac)
        return new
    def changeColor(self, color):
        self.clr = color
    def printCat(self):
        print(f"{self.clr} is {self.ac}")
# DRIVE CODE
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
