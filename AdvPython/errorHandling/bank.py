class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.balance -= amount
        print("Withdraw success")

# Handle the error
try:
    acc = BankAccount(2000)
    acc.withdraw(2222)
except InsufficientBalanceError as e:
    print(f"Error: {e}")
    print(f"Your current balance is: {acc.balance}")