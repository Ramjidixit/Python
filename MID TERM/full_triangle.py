#to print full triangle in star pattern
rows = int(input('Enter the number of rows:  '))
col = 2*rows-2
for i in range(0,rows,1):
    for j in range(0,col,1):
        print(end=" ")
    col -=1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")