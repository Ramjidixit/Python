#counting the frequency of a  character in a string
'''a= input('Enter the string:  ')
b= input('Enter the character to be counted:  ')
print(a.count(b))'''
#counting the frequency of all  character in a string
a = input('Enter the string:  ')
frequency_counter = {}
for i in a:
    keys = frequency_counter.keys()
    if i in keys:
        frequency_counter[i] += 1
    else:
        frequency_counter[i] = 1

print(frequency_counter)