# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct the specified amount if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
