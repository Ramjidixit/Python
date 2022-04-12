#remove duplicate from the given list
original = eval(input('Enter the element: '))
new = []
for i in original:
    if i not in new:
        new.append(i)
print(new)