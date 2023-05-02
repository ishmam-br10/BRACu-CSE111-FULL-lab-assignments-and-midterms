# TASK 2 vallage naaaa ... Sad catto meows :(

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def __str__(self):
        return '(' + str(self.x) + ' , ' + str(self.y) + ')'


# write your code here

class Vehicle2010(Vehicle):
    def moveLowerLeft(self):
        self.moveDown()
        self.moveLeft()

    def moveUpperRight(self):
        self.moveUp()
        self.moveRight()

    def moveUpperLeft(self):
        self.moveUp()
        self.moveLeft()

    def moveLowerRight(self):
        self.moveLeft()
        self.moveRight()

    def equals(self, new):
        return self.x == new.x and self.y == new.y


print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))