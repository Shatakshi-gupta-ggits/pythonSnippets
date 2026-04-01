'''
ce - class - inherits from exception 
'''
class InvalidAgeError(Exception):
    pass
def check_age(age):
        if age < 18:
         raise InvalidAgeError("Age must be 18 or above")
        print("Access granted")
        
try:
    check_age(10)
except InvalidAgeError as e:
        print("Custom error caught")