class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        print("Processing payment of:", self.amount)
        
class CreditCardPayment(Payment):
    pass
    
class UPIPayment(Paymemt):
    pass

p1 = CreditCardPayment 