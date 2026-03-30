'''def greet(name = "Coder"):
    print("Hello : ", name)
    
greet()

def introduce(name, age):
    print("Name ", name, "Age", age)

# introduce("rahul", 23)
introduce(23, "pappu") '''
# name = 23 , age = pappu

''' KEY Word Arguments
*arg  = collects positional arguments only in the tuple

**keyargs = 
'''
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(10, 20, 30))

