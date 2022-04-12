#to print fibbonacci series
n = int(input('Enter the number of terms to be displayed'))
first = 0
second = 1
if n ==1:
    print(f'The fibonacci series for {n} term is: {first}')
elif n==2:
    print(f'The fibonacci series for {n} term is: {first, second}')
elif n==0:
    print(f'The fibonacci series has no terms')
else:
    print(f'The fibonacci series for {n} term is: \n{first}, {second}, ',end='')
    while(n>2):
        third = first + second
        print(f'{third}, ',end='')
        first = second
        second = third
        n -=1