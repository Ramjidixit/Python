#Write a python program to calculate profit or loss. 
c=int(input("Enter the cost price:"))
s=int(input("Enter the selling price:"))
if(s>c):
    print("Profit=",s-c)
else:
    print("Loss=",c-s)