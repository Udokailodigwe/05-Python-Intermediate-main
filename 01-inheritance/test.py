import unittest
from bankaccount import Customer, Account


class TestCustomer(unittest.TestCase):
    def test_init(self):
        customer = Customer("Udoka", "Helsinki, Finland")
        self.assertEqual(customer.name, "Udoka")
        self.assertEqual(customer.address, "Helsinki, Finland")


class TestAccount(unittest.TestCase):
    def test_init(self):
        customer = Customer("Udoka", "Helsinki, Finland")
        account = Account( "1234567", customer, 500000)
        self.assertEqual(account.account_number, "1234567")
        self.assertEqual(account.customer, customer)
        self.assertEqual(account.balance, 500000)

    def test_successful_deposit(self):
        account = Account("1234567", "Udoka", 5000)
        amount = 1000
        expected = f"Deposited ${amount:.2f}. New balance: ${account.balance + amount:.2f}"
        self.assertEqual(account.deposit(amount), expected)
        self.assertEqual(account.balance, float(6000))

    def test_unsuccessful_deposit(self):
        account = Account("1234567", "Udoka", 5000)
        amount = 0
        expected = "Invalid deposit amount."
        self.assertEqual(account.deposit(amount), expected)
        self.assertEqual(account.balance, 5000)


    def test_successful_withdraw(self):
        account = Account("1234567", "Udoka", 5000)
        amount = 1000
        expected = f"Withdrew ${amount:.2f}. New balance: ${account.balance - amount:.2f}"
        self.assertEqual(account.withdraw(amount), expected)
        self.assertEqual(account.balance, float(4000))

    def test_unsuccessful_withdraw(self):
        account = Account("1234567", "Udoka", 0)
        amount = 1000
        expected = "Invalid withdrawal amount or insufficient balance."
        self.assertEqual(account.withdraw(amount), expected)
        self.assertEqual(account.balance, 0)

    def test_check_balance(self):
        account = Account("1234567", "Udoka", 2000)
        self.assertEqual(account.check_balance(), f"Account balance: ${account.balance}")

################### ANOTHER SOLUTION  ##########

# class TestAccountMethods(unittest.TestCase):
#     def setUp(self):
#         self.customer = Customer("Tolulope Ademilua", "123 Tallinn, Tallinn")
#         self.account = Account("123456", self.customer)
#
#     def test_initial_balance(self):
#         self.assertEqual(self.account.balance, 0.0)
#
#     def test_deposit(self):
#         self.account.deposit(1000)
#         self.assertEqual(self.account.balance, 1000.0)
#
#     def test_withdraw_valid_amount(self):
#         self.account.deposit(1000)
#         self.account.withdraw(200)
#         self.assertEqual(self.account.balance, 800.0)
#
#     def test_withdraw_invalid_amount(self):
#         self.account.deposit(1000)
#         self.account.withdraw(1200)
#         self.assertEqual(self.account.balance, 1000.0)  # Balance should remain unchanged
#
#     def test_check_balance(self):
#         self.account.deposit(1000)
#         self.assertEqual(self.account.check_balance(), "Account balance: $1000.00")
#
# if __name__ == '__main__':
#     unittest.main()