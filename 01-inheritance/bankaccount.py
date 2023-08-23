"""
This homework will check you python fundamental skills and object-oriented programming concepts.
Please fill in the missing code. I added it as a comment with the code
Also in place of self..., you will have to set it up correctly.
If you scroll down to line 44, The expected result is what I have added as the output.
Once you achieved the result. Please write a unittest also to test the application.
"""


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Account:
    def __init__(self, account_number, customer, balance):
        self.account_number = account_number
        self.customer = customer
        self.balance = float(balance)

    def deposit(self, amount):
        # pls put the logic to increment the balance here based on the amount added
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            print("Invalid deposit amount.")
            return "Invalid deposit amount."

    def withdraw(self, amount):
        # put the logic to handle the withdrawal here
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            print("Invalid withdrawal amount or insufficient balance.")
            return "Invalid withdrawal amount or insufficient balance."

    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        return f"Account balance: ${self.balance}"


# Creating a customer
customer1 = Customer("Tolulope Ademilua", "123 Tallinn, Tallinn")

# Creating an account for the customer
account1 = Account("123456", customer1, 0)

# Depositing and withdrawing from the account

account1.deposit(1000)
account1.withdraw(200)
account1.check_balance()

# Output:
# Deposited $1000. New balance: $1000
# Withdrew $200. New balance: $800
# Account balance: $800
