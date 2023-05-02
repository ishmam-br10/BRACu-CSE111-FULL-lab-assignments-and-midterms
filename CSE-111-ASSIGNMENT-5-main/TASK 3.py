class Team:
    def __init__(self, name = ''):
        self.__team = name
        self.__players = []

    def addPlayer(self, add):
        self.__players.append(add.player)

    def setName(self, team):
        self.__team =team

    def printDetail(self):
        print('=====================')
        print(f'Team: {self.__team}')
        print('List of Players: ')
        print(f'{self.__players}')
        print('=====================')

class Player:
    def __init__(self, player):
        self.player = player

## DRIVER CODE
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
