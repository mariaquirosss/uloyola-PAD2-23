class BankAccount:
    def __init__(self, #TODO):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance
        self.account_type = account_type

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_holder(self):
        return self.holder

    def set_holder(self, holder):
        self.holder = holder

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def deposit(self, amount):
        ## TODO

    def withdraw(self, amount):
        ## TODO

    def print_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ${self.balance}")

# Example usage of the BankAccount class:
account = BankAccount("11111111", "John Doe", 1000.0, "Pensiones")
account.print_balance()
##
# Account Number: 11111111
# Account Holder: John Doe
# Account Type: Pensiones
# Current Balance: $1000.0

account.deposit(500)
# Deposited $500. New balance: $1500.0
account.withdraw(200)
# Withdrew $200. New balance: $1300.0
