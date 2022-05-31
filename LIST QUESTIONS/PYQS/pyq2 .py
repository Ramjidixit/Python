"""write a test program that prompts the user to enter a list and displays 
whether the list is sorted or not"""
a=eval(input("enter the list:"))
b=a.copy()
print(b)
b.sort()
print(b)
if (a==b):
    print("The list is already sorted")
else:
    print("The list is not sorted.")

