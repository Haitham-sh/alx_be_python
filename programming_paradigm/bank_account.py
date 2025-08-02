class BankAccount:
    def __init__ (self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}. ")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}.")