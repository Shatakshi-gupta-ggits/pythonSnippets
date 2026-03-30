class BankAccount:
    def __init__(self, name, balance):
        self.name = name,
        self.balance = balance
        
acc1 = BankAccount("Pappu", 10000)
acc1.balance = 100000
print(acc1.name, acc1.balance)
