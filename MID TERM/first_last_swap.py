#Python program to change a given string to a new string where the first and last chars have been exchanged.
a = input('Enter the string:  ')
print(f'The string brfore swapping is: {a}')
a = a[-1] + a[1:-1] + a[0]

print(f'The string after swapping is:  {a}')