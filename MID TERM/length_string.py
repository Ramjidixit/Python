#program to calculate the length of a string
a= input('Enter a string: ')

print(f'The length of the string is: {len(a)}')
count = 0
for i in a:
    count = count + 1

print(f'The length of the string is {count}')