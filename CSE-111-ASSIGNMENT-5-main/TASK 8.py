class Coordinates:
    def __init__(self, or1, or2):
        self.__ordinate1 = or1
        self.__ordinate2 = or2
        self.details = (or1, or2)

    def detail(self):
        return ((self.__ordinate1, self.__ordinate2))
    def __sub__(self, other):
        return Coordinates(self.__ordinate1- other.__ordinate1, self.__ordinate2 - other.__ordinate2)

    def __mul__(self, other):
        return Coordinates(self.__ordinate1*other.__ordinate1, self.__ordinate2*self.__ordinate2)

    def __eq__(self, other):
        if self.details == other.details:
            return ('The calculated coordinates are the same.')
        else:
            return('The calculated coordinates are not the same.')

# DRIVER CODE
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)
