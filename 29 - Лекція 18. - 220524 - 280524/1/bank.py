from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, initial_balance):
        new_account = Account(initial_balance)
        self.accounts[account_number] = new_account
        return new_account

    def get_account(self, account_number):
        return self.accounts.get(account_number)