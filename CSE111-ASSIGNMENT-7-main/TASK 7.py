# TASK 7

class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(SportsPerson):
  def __init__(self, club, player, role, goal, match):
    super().__init__(club, player, role)
    self.goal = goal
    self.match = match
    self.ratio = 0
    self.earning_per_match = (goal * 1000)+ (match * 10)
  def calculate_ratio(self):
    self.ratio = self.goal / self.match
  def print_details(self):
    print(f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Goal:{self.goal}\nTotal Played: {self.match}"
            f"\nGoal Ratio: {self.ratio}\n Match Earning: {self.earning_per_match}k")

class Manager(SportsPerson):
  def __init__(self, club, manager, role, match):
    super().__init__(club, manager, role)
    self.match = match
    self.earning_per_match = match * 1000
  def print_details(self):
    print (f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Win: {self.match}\nMatch Earning: {self.earning_per_match}")

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
