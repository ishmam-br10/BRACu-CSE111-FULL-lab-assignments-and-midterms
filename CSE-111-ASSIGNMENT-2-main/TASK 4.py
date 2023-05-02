class Pokemon:
    def __init__(self, pokemon1, pokemon2, poke1_pow, poke2_power
                 , damage):
        self.pokemon1_name = pokemon1
        self.pokemon2_name = pokemon2
        self.pokemon1_power = poke1_pow
        self.pokemon2_power = poke2_power
        self.damage_rate = damage
# DRIVER CODE
# TEAM PIKACHU
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
## TEAM BULBASUR
print("=======Team 2=======")
team_bulb = Pokemon('bulbasur', 'squirtle', 80, 70, 9)
print('Pokemon 1:',team_bulb.pokemon1_name,
team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,
team_bulb.pokemon2_power)
bulb_combined_power = (team_bulb.pokemon1_power +
team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', bulb_combined_power)
