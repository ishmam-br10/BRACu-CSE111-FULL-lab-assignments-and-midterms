class animal:
    def __init__(self, name):
        self.name = name
        self.color = "White"
    def eat(self):
        print(f"{self.color} {self.name} is eating")

#============================================================

class dog(animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color          #recreating the parent variable here again
    def bark(self):
        print(f"{self.color} {self.name} is barking")

#======= Command line ============
d1 = dog("Rocket", "Brown")
d1.eat()
d1.bark()