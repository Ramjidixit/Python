#to print sum upto upper limit
n = int(input('Enter the upper limit of sum:  '))
sum = 0
for i in range(1,n+1):
    sum += i
print(f'The sum of all natural upto {n} is {sum}')