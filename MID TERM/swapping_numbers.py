# Swapping two numbers using a temporary variable
'''a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

temp = a
a = b
b = temp

print('The first number is now: ', a)
print('The second number is now: ', b)'''

#Swapping two numbers without using a temporary variable
'''a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
a = a+b
b = a-b
a = a-b
print('The first number is now: ', a)
print('The second number is now: ', b)'''

#Swapping two numbers using bitwise operators
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
a = a^b
b = a^b
a = a^b
print('The first number is now: ', a)
print('The second number is now: ', b)