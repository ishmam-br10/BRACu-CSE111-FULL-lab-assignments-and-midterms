class Joker:
    def __init__(self, name, power, psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = psycho


# DRIVER CODE
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print('=====================')
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print('=====================')
if j1 == j2:
 print('same')
else:
 print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
 print('same')
else:
 print('different')
# EXPLANATION FOR SUBTASK 2, 3

print(f"Every object created has a different memory location so the first one prints 'Different'")
print(f"When we update j2.name and check the Equality then it prints same cause 'Heath Ledger'")