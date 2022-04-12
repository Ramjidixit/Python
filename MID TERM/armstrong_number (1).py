#to cjeck whether the number is armstrong or not
a = int(input('Enter the number to be checked: '))
temp = a
sum = 0
count = 0
while(temp>0):
    temp //= 10
    count += 1
temp = a
while(a>0):
    digit = a%10
    sum += digit**count
    a //= 10
if(sum == temp):
    print('The number is an Armstrong number')
else:
    print('The number is not an Armstrong number')