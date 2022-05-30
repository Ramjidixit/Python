"""Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not"""
try:
    a=int(input())
    b=int(input())
    c=a/b 
    print(c)
except :
    print("zerodivisionerror")
else:        # the try block does not generate any error:
    print("Everything is correct bro")