"""wap to enter a string and check whether it is palindrome or not"""
s=input("Enter the string:")
a=s[::-1]
if(s==a):
    print("The given string is palindrome.")
else:
    print("The given string is not a palindrome.")