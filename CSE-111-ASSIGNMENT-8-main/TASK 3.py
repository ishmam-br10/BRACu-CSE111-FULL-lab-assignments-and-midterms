class Account:
    def __init__(self, balance):
        self._balance = balance

    def getBalance(self):
        return self._balance

class CheckingAccount(Account):
     numberOfAccount = 0
     def __init__(self, taka = 0):
         CheckingAccount.numberOfAccount += 1
         super().__init__(taka)
     # def numberOfAccount(self):
     #     return str(CheckingAccount.number)
     def __str__(self):
         return f"Account Balance: {(super().getBalance())}"

print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
