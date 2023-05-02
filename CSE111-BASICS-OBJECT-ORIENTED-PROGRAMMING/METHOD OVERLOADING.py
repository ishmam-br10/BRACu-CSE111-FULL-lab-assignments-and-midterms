from multipledispatch import dispatch
class players:
    @dispatch(str, int)
    def goals(self, a,b):
        print(a, 'scored at ', b, 'minutes')
    @dispatch(str, str, int)
    def goals(self, a,b,c):
        print(a, 'charged for foul and received ', b, ' at ',c, ' minutes.')
    @dispatch(str, int, str)
    def goals(self, a, b, c):
        print(a, ' got substituted at ', b, ' minutes ', ' by ', c)

#===========================================
inp = input("Announcement: ")
if inp == 'goal':
    goal_scorer = input("Goal Scorer: ")
    minute = int(input("minute: "))
    score = players()
    score.goals(goal_scorer, minute)
elif inp == 'card':
    card_holder = input("Card holder : ")
    minute = int(input('Minute: '))
    card = input("Card name: ")
    score = players()
    score.goals(card_holder, card, minute)
elif inp == 'sub':
    subbed = input("Subbed player: ")
    minute = int(input('Minute: '))
    on_field = input("Player on field: ")
    score = players()
    score.goals(subbed, minute, on_field)
# score = players()
# score.goals(goal_scorer, minute)
# score.goals(card_holder, card, minute)
# score.goals(subbed, minute , on_field)