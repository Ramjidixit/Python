#TO FIND factorial of any given number
a = int(input('Enter the number whose factorial is to be found:  '))
b=a
fact =1
while(a>0):
    fact = fact*a
    a -=1
print(f'The factorial of {b} is: {fact}')