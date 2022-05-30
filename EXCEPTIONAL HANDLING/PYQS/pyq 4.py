"""difference between error and exception
Errors are the problems in a program due to which the program will stop the execution. 
On the other hand, exceptions are raised when some internal events occur which changes 
the normal flow of the program. 
Two types of Error occurs in python. 
Syntax errors
Logical errors (Exceptions)

#multiple except block
It is possible to have multiple except blocks for one try block. 
Let us see Python multiple exception handling examples.
a,b=1,0
try:
    print(a/b)
    print("This won't be printed")
    print('10'+10)
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")
    
    
#try except block 
When you think a part of your code might throw an exception, put it in a try block.
Let us see a Python try exception example.
try:
    for i in range(3):
    print(3/i)
except:
    print("You divided by 0")
    print(‘This prints because the exception was handled’)"""