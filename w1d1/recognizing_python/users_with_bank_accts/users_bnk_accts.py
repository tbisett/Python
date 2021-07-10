class BankAccount:
    # bankName = "First National Dojo"
    all_accounts = []
    
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def display_account_info(self):
        print(f'"balance" = {self.balance}')
        return self

    def yield_interest(self):
        newBalance = self.balance + (self.balance * 0.02)
        self.balance = newBalance
        return self

    @classmethod
    def sum_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @staticmethod
    def can_withdraw(balance, amount):
        return balance - amount >= 0
         


class user:
    
    def __init__(self, name, account):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_withdrawal(self, amount):
        self.account.withdraw()
        # print(self.account_balance)

    def display_user_balance(self):
        print(self.account.balance())

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    def make_deposit(self):
        self.account.deposit()
        

taylor = user("Taylor", 100)
cameron = user("Cameron", 0)
# tarra = user()
# steve = user()
taylor.account.deposit(500)
taylor.account.deposit(500)
taylor.account.withdraw(250)
cameron.account.deposit(1000)
print(taylor.account.balance)
print(BankAccount.sum_all_balances())

