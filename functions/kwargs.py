#  *args and **kwargs are used in function definitions to handle a variable number of arguments. 
# W3Schools
# W3Schools
#  +1
# *args collects an arbitrary number of positional (non-keyword) arguments into a tuple.
# **kwargs collects an arbitrary number of keyword arguments into a dict (dictionary). 


def my_function(arg1, *args, **kwargs):
    print("First regular argument:", arg1)
    print("Positional arguments (tuple):", args)
    print("Keyword arguments (dictionary):", kwargs)

# Calling the function
my_function("required", 1, 2, 3, name="John", age=30)

# First regular argument: required
# Positional arguments (tuple): (1, 2, 3)
# Keyword arguments (dictionary): {'name': 'John', 'age': 30}

def print_args(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

my_list = [1, 2, 3]
print_args(*my_list) # Unpacks the list into positional arguments

my_dict = {'a': 10, 'b': 20, 'c': 30}
print_args(**my_dict) # Unpacks the dictionary into keyword arguments

# Flexibility: Allows functions to adapt to various use cases without needing to be rewritten for different numbers of inputs.
# Common Use Cases: Frequently used in decorators, function wrappers, and class inheritance (super()) to pass arguments down the chain.
# Readability: Can enhance code readability by naming arguments explicitly with **kwargs but overuse can lead to complexity and harder debugging.
# Data Types: args is a tuple and kwargs is a dictionary. 
