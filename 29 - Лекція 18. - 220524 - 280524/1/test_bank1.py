import unittest
from bank1 import Bank

class TestBank(unittest.TestCase):
    
    def setUp(self):
        self.bank = Bank()
    
    def test_open_account(self):
        account_number = '12345'
        initial_balance = 100.0
        
        account = self.bank.open_account(account_number, initial_balance)
        
        fetched_account = self.bank.get_account(account_number)
        
        self.assertIsNotNone(fetched_account, "Account should be opened and not None.")
        
        self.assertEqual(fetched_account.get_balance(), initial_balance, "Initial balance should be set correctly.")
        
        self.assertIs(account, fetched_account, "The account object should be the same as the fetched account object.")

if __name__ == '__main__':
    unittest.main()