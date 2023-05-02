class Cat:
    def __init__(self, color = 'White', action = 'sitting'):
        self.color = color
        self.action = action

    def printCat(self):
        print(f"{self.color} cat is {self.action}")
    def changeColor(self, cl):
        self.color = cl
# driver code
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
