class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

class SavingsAccount(Account):
    def __init__(self, balance, interest):
        super().__init__(balance)
        self.interest = interest

    def add_interest(self):
        self.balance += self.balance * self.interest

class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit