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
