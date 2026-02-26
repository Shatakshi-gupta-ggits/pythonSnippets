# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.
# range(start, stop, step)


x = range(3, 10, 2)

#display x:
#print(x)

#convert to list to display the content of x:
#print(list(x))

# for i in range(10):
#   print(i)
  
# print(list(range(5)))
# print(list(range(1, 6)))
# print(list(range(5, 20, 3)))

# slicing ranges
# r = range(10)
# print(r[2])
# print(r[:3])

r = range(0, 10, 2)
# print(6 in r) --true
# print(7 in r)  -- false

r = range(0, 10, 2)
print(len(r))
