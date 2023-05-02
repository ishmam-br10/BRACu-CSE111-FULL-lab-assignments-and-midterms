class Shape3D:

  pi = 3.14159
  def __init__(self, name = 'Default', radius = 0):
    self._area = 0
    self._name = name
    self._height = 'No need'
    self._radius = radius

  def calc_surface_area(self):
    return 2 * Shape3D.pi * self._radius

  def __str__(self):
      return "Radius: "+str(self._radius)
# MY CODE HERE
class Sphere(Shape3D):
    def __init__(self, name= 'Sphere', rad=0):
        super().__init__(name, rad)
        print(f"Shape name: {self._name}, Area Formula: 4 * pi * r * r")
    def calc_surface_area(self):
        self.area = f"Radius: {self._radius}, Height: {self._height}\n"\
               f"Area: {4* 3.14159 * self._radius ** 2}"
    def __str__(self):
        return self.area
class Cylinder(Shape3D):
  def __init__(self,name,radius,h):
    print("Shape name: Cylinder, Area Formula: 2*pi*r*(r+h)")
    super().__init__(name,radius)
    self.h =h
  def get_r(self):
    return self._radius
  def calc_surface_area(self):
    return f"{super().calc_surface_area()*(self.get_r()+self.h)}"
  def __str__(self):
    return (f"{super().__str__()}, Height: {self.h}\nArea:{self.calc_surface_area()}")
sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)
