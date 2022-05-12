#Write a program to find the maximum of two numbers.
def max(m,n):
    print("first number=",m)
    print("second number=",n)
    if m>n:
        print("maximum number=",m)
    elif(m<n):
        print("maximum number=",n)
    else:
        print("Equal")
max(16,85)