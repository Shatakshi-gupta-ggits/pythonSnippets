'''create a function that 
input - number n 
even numbers from 1 to n
return

10 

1- 10
2 4 6 8 10
%2 == 0

5

loop. > 1 to n
if > even
function > logic
return
'''
def count_even(n):
    count = 0
    for i in range(1, n+1):
        if i%2 == 0:
            print(i)
            count += 1
        return count
    
result = count_even(10)
print(result)
