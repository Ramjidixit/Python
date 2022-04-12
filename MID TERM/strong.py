#to check whether the number is strong number or not
n = int(input('Enter the number to be checked:  '))
m = n
sum = 0
while(m>0):
    rem  = m%10
    fact = 1
    while(rem>0):
        fact *=rem
        rem -=1
    sum = sum+fact 
    m //=10
if sum==n:
    print(f'{n} is a Strong Number')
else:
    print(f'{n} is not a Strong Number')