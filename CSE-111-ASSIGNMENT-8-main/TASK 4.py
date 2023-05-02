class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin


class testFruit:
    def test(self, f):
        print('----Printing Detail----')

        if f.hasFormalin():
            print('Do not eat the', f.getName(), '.')
            print(f)
        else:
            print('Eat the', f.getName(), '.')
            print(f)

class Mango(Fruit):
  def __init__(self):
    super().__init__(True,"Mangos")
   # self.name = "Mango"
  def __str__(self):
    return f"{self.getName()} are bad for you"

class Jackfruit(Fruit):
  def __init__(self,formalin = True,name="Jackfruits"):
    super().__init__(formalin,name)#Eat the jackfruit hobe not plural
  def __str__(self):
    return f"{self.getName()} are good for you"
m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)