"""WAP that prompts the user to enter a number.
If the number is positive or zero, print it, other wise raise an exception Value 
Error with some message."""
a=int(input("Enter the number:"))
try:
    if(a<0):
        raise ValueError 
    else:
        print(a)
except ValueError:
    print("Please check the number again.")
