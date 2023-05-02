class Shape:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def area(self):
        if self.name == 'Triangle':
            self.area = str(.5 * self.a * self.b)
        elif self.name == 'Square':
            self.area = str(self.a ** 2)
        elif self.name == 'Rectangle':
            self.area = str(self.a * self.b)
        elif self.name == 'Rhombus':
            self.area = str(self.a * self.b *0.5)
        else:
            self.area = 'Shape is unknown'
        print(f"Area: {(self.area)}")
# driver code
triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()
