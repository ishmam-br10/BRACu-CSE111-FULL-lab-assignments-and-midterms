
## METHOD OVERRIDING

class parent:
    def __init__(self):
        print("__init__ of parents")
    # def method1(self):
    #     print("always study")
    def method1(self):
        print("Olpo study")
    def method2(self):
        print("You will get all of my properties and methods")

class child(parent):

    def __init__(self):
        #print("__init__ of child")
        pass
    # def method1(self):
    #     print("Always movies")
    def method1(self):
        super().method1()
        print("Always movies")
c1 = child()
c1.method1()
c1.method2()
