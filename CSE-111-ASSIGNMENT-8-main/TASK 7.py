class PokemonBasic:

  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type

  def get_type(self):
    return 'Main type: ' + self.type

  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'

  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness
##  MY CODE HERE
class PokemonExtra(PokemonBasic):
  def __init__(self, name1, hp1, weak1, type1, type2 = None, moves = None):
      self.move = moves
      self.type2 = type2
      super().__init__(name1, hp1, weak1, type1)

  def get_type(self):
    if self.type2 == None:
      return 'Main type: ' + self.type
    else:
      return f"Main type: {self.type}, Secondary type: {self.type2}"

  def get_move(self):
    if self.move == None:
      return 'Basic move: ' + 'Quick Attack'
    else:
      return f"Basic move: Quick Attack\nOther move: {', '.join(self.move)}"

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
