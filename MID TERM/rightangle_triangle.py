#to print right angle triangle of * printing
row = int(input('Enter the number of rows: '))
for i in range(0,row):
    for j in range(0,i):
        print(" * ",end='')
    print('\n')
     