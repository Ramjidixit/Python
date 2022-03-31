"""Wap to enter the string and then find the length of the string (a)using predefined operator 
(b)without using predefined function"""

b=input("Enter the string:")
a=len(b)
print("The length of the given string using predefined operator is=",a)
counter=0
for s in b:
    counter=counter+1 
print("The length of the given string without using predefined function=",counter)