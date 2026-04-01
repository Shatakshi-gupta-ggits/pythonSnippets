#Abstracttion - hidng the unneccessary data (complexity)
# hide implementation method
# class Payment():
#     def pay(self):
#         print("Processing payment")
        
# p = Payment()
# p.pay()
'''
class Animal():
    def sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    def sound(self):
        print("Bark bark..")
              
              
class Cat(Animal):
 def sound(self):
   print("Meaaaww...")

animals = [Dog(), Cat()]
for a in animals:
    a.sound() '''

    
from abc import ABC, abstractmethod

class Animal(ABC):
    def sound(self):
        print()