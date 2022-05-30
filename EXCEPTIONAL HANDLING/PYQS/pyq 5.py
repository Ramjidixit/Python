"""how many except blocks are allowed with one try block in python 
It is possible to have multiple except blocks for one try block. 
Let us see Python multiple exception handling examples. 
When the interpreter encounters an exception, it checks the except blocks associated with that try block.
>>> a,b=1,0
>>> try:
          print(a/b)
          print("This won't be printed")
          print('10'+10)
except TypeError:
          print("You added values of incompatible types")
except ZeroDivisionError:
          print("You divided by 0")"""
