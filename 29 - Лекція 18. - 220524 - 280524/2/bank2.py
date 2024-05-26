from account2 import Account, SavingsAccount, CurrentAccount

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def update(self):
        for acc in self.accounts:
            if isinstance(acc, SavingsAccount):
                acc.add_interest()
            elif isinstance(acc, CurrentAccount) and acc.get_balance() < 0:
                print("Letter sent to CurrentAccount holder about overdraft")
                