class BankAccount:
    def __init__(self, account_number="0000", holder="Unknown", balance=0.0, account_type="Type"):
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

# Deposited $500. New balance: $1500.0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def print_balance(self):
        print("Account Information:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: ${self.balance:.2f}")

# Example usage:
account = BankAccount("11111111", "John Doe", 1000.0, "Pensiones")

account2 = BankAccount()
account.print_balance()
# Account Number: 11111111
# Account Holder: John Doe
# Account Type: Pensiones
# Current Balance: $1000.0

account.deposit(500)
# Deposited $500. New balance: $1500.0
account.withdraw(200)
# Withdrew $200. New balance: $1300.0
