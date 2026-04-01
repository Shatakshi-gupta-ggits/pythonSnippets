#Encap = protection + control
# binding data and methods inside a class , limited and controlled access

class BankAccount:
    def __init__(self, name, balance):
        self.name = name,
        self.__balance = balance #private variable
        
    # self.balance - public
    
    # self._balance - protected
    # self.__balance - private
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self, amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
        else:
            print("In-valid withdrawl")
            
    def get_balance(self):
        return self.__balance
    
acc1 = BankAccount("Pappu", 10000)
print("1st", acc1.get_balance())
acc1.deposit(5000)
acc1.___balance = 110000
print("After deposit 5000", acc1.get_balance())
acc1.withdraw(2000)
print("After withdraw", acc1.get_balance())
# acc1.balance = 100000
print(acc1.__balance)

_BankAccount_