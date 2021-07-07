

class user:
    
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        # print(self.account_balance)
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

taylor = user("Taylor", 100)
cameron = user("Cameron", 0)
# tarra = user()
# steve = user()

taylor.make_withdrawal(30).display_user_balance().transfer_money(cameron, 70).display_user_balance()
