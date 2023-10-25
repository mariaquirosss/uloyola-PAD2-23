class BankAccount:
    def __init__(self, account_number="", holder="", balance=0.0, account_type="Savings"):
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
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal. Either the amount is invalid or insufficient funds.")

    def print_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ${self.balance}")

# Example usage of the BankAccount class:
account = BankAccount("11111111", "John Doe", 1000.0, "Pensiones")
account.print_balance()

account.deposit(500)
account.withdraw(200)
