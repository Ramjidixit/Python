
#Program to count the frequency of words in a given string
a = input('Enter the string:  ')
frequency_counter = {}
for i in a.split():
    keys = frequency_counter.keys()
    if i in keys:
        frequency_counter[i] += 1
    else:
        frequency_counter[i] = 1
print(frequency_counter)