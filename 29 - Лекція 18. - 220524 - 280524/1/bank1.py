from account1 import Account, SavingsAccount, CurrentAccount

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, initial_balance):
        account = Account(account_number, initial_balance)
        self.accounts[account_number] = account
        return account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts.values():
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)