'''
The following program demonstrate the addition of first and last digit of a given number.
input.
The program will ask the user to enter a number and will add the first and last digit of the number.
The number of input is stored in a list 
'''
number_of_input = int(input('Enter the number of inputs you want'))
lis  = []
for i in range(0,number_of_input):
    num = int(input('Enter the number: '))
    lis.append(num)
print(f'The input is {lis}')
result = []
for i in lis:
    temp2= i
    temp = i
    count = 0
    while (temp2>0):
        count +=1
        temp2 //=10
    if count==1 or count==0:
        result.append(i)
    else:
        temp = i
        last = temp%10
        while(temp>0):
            first = temp%10
            temp //=10
        sum = first + last
        result.append(sum)
print(f'The sum is {result}')