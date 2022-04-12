#to print armstrong numbers in range
lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))
for num in range(lower, upper+1):
    sum = 0
    temp = num
    count = 0
    while(temp>0):
        temp //= 10
        count += 1
    temp = num
    while(num>0):
        digit = num%10
        sum += digit**count
        num //= 10
    if(sum == temp):
        print(f'{temp} is an Armstrong number')