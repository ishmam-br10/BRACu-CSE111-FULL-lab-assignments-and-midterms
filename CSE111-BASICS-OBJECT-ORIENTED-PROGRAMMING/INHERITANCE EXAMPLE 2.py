class parent():      # Parent cell
    def method1(self):
        print("Parent cell executed")

class child1(parent):       #Child cell 1
    def method2(self):
        print("Child 1 cell executed")


class child2(child1):       #Child cell 2
    def method3(self):
        print("Child 2 cell executed")

class child3(child2):       #Child cell 3
    def method4(self):
        print("Child 3 cell executed")


################ COMMAND LINE #############
p1 = parent()
c1 = child1()
c2 = child2()
c3 = child3()
p1.method1()
c1.method2()
c2.method3()
c3.method4()

# parent class cannot access child inheritence
# p1.method2()
