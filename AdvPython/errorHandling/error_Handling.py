'''
try 
except
else -  #tabhi chalega jab koi error nhi hoga 
finally - error ho na ho jarurur chalega 

'''
try:
    x = int(input("Enter a number:"))
    # print(10/x)
    result = 10/x
    
except ZeroDivisionError:
    print("You can not devide with zero")
 

   
except ValueError:
    print("Provide right value")
    
except TypeError:
    print("You cannot devide with string.. ")
    
    
else:
    print("Result: ", result)
    
finally:
    print("Program execution done, reuslt :", result)