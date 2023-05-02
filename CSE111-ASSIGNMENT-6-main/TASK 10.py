class SultansDine:
    branch = 0
    sell =0
    branches = []
    @classmethod
    def details(cls):
        print(f'Total number of branch(s):{cls.branch}')
        print(f'Total Sell: {cls.sell} Taka')

    def __init__(self, branch):
        SultansDine.branch += 1
        self.branch = branch
        self.sell = 0
        SultansDine.branches.append(self)
    def sellQuantity(self, amount):
        self.sell = amount * 400
        SultansDine.sell += amount*400

    def branchInformation(self):
        pass


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
