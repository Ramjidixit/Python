#Write a C program to input angles of a triangle and check whether triangle is valid or not. 
a=int(input("Enter the first angle in degree:"))
b=int(input("Enter the second angle in degree:"))
c=int(input("Enter the third angle in degree:"))
if(a+b+c==180):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")