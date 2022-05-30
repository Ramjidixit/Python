#wap which explains ZeoDivisionError.
try:
    a=int(input("Enter the number:"))
    b=int(input("enter the b:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("check b")
    
