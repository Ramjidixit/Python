#Program for removing character from a given string
a = input('Enter the string:  ')
b = input('Enter the character to be removed:  ')
a = a.replace(b, '',1)
print(a)

#Program for removing character of a given index from a given string
'''a = input('Enter the string:  ')
b = int(input('Enter the index of the character to be removed:  '))
a = a[:b] + a[b+1:]
print(a)'''

