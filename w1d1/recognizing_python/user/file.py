

class user:
    
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        # print(self.account_balance)

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        

taylor = user("Taylor", 100)
cameron = user("Cameron", 0)
# tarra = user()
# steve = user()

taylor.make_withdrawal(30)
taylor.display_user_balance()
taylor.transfer_money(cameron, 70)
cameron.display_user_balance()