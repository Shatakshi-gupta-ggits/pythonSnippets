class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        print("Processing payment of:", self.amount)
 
 #Polymorphism
      
class CreditCardPayment(Payment):
    def pay(self):
        print("Credit card payment of:", self.amount, "with 10% fees")
    
class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment of", self.amount, "With no fees")
    pass

p1 = CreditCardPayment(500)
p1.pay()

p2 = UPIPayment(200)
p2.pay()