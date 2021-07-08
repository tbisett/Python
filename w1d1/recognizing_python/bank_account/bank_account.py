class BankAccount:
    # all_accounts = []
    
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'"balance" = {self.balance}')
        return self

    def yield_interest(self):
        newBalance = self.balance + (self.balance * 0.02)
        self.balance = newBalance
        return self

# @classmethod
# def sum_all_balances(cls):
#     sum = 0
#     for account in cls.all_accounts:
#         sum += account.balance
#     return sum



account1 = BankAccount(0.02, 0)
account2 = BankAccount(0.02, 0)

# account1.deposit(100), account1.deposit(100), account1.deposit(50), account1.withdraw(50), account1.yield_interest(), account1.display_account_info()
account1.deposit(100).deposit(100).deposit(50).withdraw(50).yield_interest().display_account_info()
account2.deposit(500).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
# print(all_accounts)