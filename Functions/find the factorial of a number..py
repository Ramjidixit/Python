#find the factorial of a number.
def calc_factorial(num):
    fact=1
    print("Entered Number is:",num)
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of Number ",num," is =",fact)
number=int(input("Enter the Number:"))
calc_factorial(number)