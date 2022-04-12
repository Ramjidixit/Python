#to find hcf and lcm of given numbers
a = int(input('Enter the first number:  '))
b = int(input('Enter the second number:  '))
if a>b:
    small = b
else:
    small = a

for i in range(small,0,-1):
    if a%i==0 and b%i==0:
        hcf = i
        break
lcm  = (a*b)/hcf
print(f'The HCF of {a} and {b} is {hcf}\nThe LCM of {a} and {b} is {int(lcm)}')