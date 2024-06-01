import unittest
from unittest.mock import patch
from bank2 import Bank
from account2 import SavingsAccount, CurrentAccount

class TestBank(unittest.TestCase):
    
    def setUp(self):
        self.bank = Bank()
    
    @patch('builtins.print')
    def test_update_accounts(self, mock_print):
        savings_account = SavingsAccount('SA123', 1000, 5.0)
        current_account = CurrentAccount('CA123', -200, 100)
        
        self.bank.open_account('SA123', 1000)
        self.bank.open_account('CA123', -200)
        
        self.bank.accounts['SA123'] = savings_account
        self.bank.accounts['CA123'] = current_account
        
        self.bank.update_accounts()
        
        self.assertEqual(savings_account.get_balance(), 1050, "Interest should be added to the savings account balance.")
        
        mock_print.assert_called_once_with("Overdraft letter sent for Account CA123")

if __name__ == '__main__':
    unittest.main()