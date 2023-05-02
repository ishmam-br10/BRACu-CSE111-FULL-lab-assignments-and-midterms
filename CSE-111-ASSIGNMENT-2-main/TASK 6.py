class Country():
    def __init__(self, name = 'Bangladesh',
                 continent = 'Asia', capital = 'Dhaka', rank = 187):
        self.name = name
        self.continent = continent
        self.capital = capital
        self.fifa_ranking = rank

# DRIVER CODE
country = Country()
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)
print('===================')
country.name = 'Belgium'
country.continent = 'Europe'
country.capital = 'Brussels'
country.fifa_ranking = 1
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)