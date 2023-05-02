import math
class Cylinder:
    radius = 5
    height = 18
    def __init__(self, rad, heig):
        print(f'Default radius: {Cylinder.radius} and height:{Cylinder.height}')
        Cylinder.radius = float(rad)
        Cylinder.height = float(heig)
        print(f'Updated: radius:{Cylinder.radius} height:{Cylinder.height}')
        self.radius = Cylinder.radius
        self.height = Cylinder.height
    @staticmethod
    def area(rad, heigh):
        print('Area: ', 2 * math.pi* rad* heigh + 2 * math.pi * rad**2 )
    @staticmethod
    def volume(rad, heigh):
        print('Volume: ', math.pi * rad ** 2 * heigh)

    @classmethod
    def swap(cls, r, h):
        new = cls(h, r)
        return new

    @classmethod
    def changeFormat(cls, one):
        det = list(map(float,one.split('-')))
        new = cls(det[0], det[1])
        return new

# DRIVER CODE
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
