# A lambda function in Python is a small, anonymous function defined using the lambda keyword. Unlike a standard function created with def, a lambda function does not require a name and is syntactically restricted to a single expression. The result of this expression is implicitly returned. 

pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
# Output: [(4, 1), (2, 2), (1, 3)]

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
# Output: [1, 4, 9, 16]

nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
# Output: [10, 20, 30]
