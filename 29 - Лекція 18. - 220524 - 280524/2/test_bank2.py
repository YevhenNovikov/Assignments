import unittest
from unittest.mock import patch
from bank2 import Bank
from account2 import SavingsAccount, CurrentAccount

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
    
    @patch('builtins.print')
    def test_update(self, mock_print):
        savings_account = SavingsAccount(1000, 0.05)
        current_account = CurrentAccount(-100, 500)

        self.bank.add_account(savings_account)
        self.bank.add_account(current_account)

        self.bank.update()

        self.assertEqual(savings_account.get_balance(), 1000 * 1.05, "Interest should be added to savings account balance.")

        mock_print.assert_called_once_with("Letter sent to CurrentAccount holder about overdraft")

if __name__ == '__main__':
    unittest.main()
    