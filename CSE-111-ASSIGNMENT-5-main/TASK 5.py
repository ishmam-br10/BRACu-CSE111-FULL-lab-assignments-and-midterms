import math
class Circle:
    def __init__(self, rad):
        self.__rad = rad

    def getRadius(self):
        return (self.__rad)

    def setRadius(self, rad):
        self.__rad = rad

    def area(self):
        return (math.pi * self.__rad ** 2)

    def __add__(self, other):
        return Circle(self.__rad + other.__rad)

# DRIVER
c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())

c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())

c3 = c1 + c2
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())
