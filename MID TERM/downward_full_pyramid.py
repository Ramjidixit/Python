#to print downward full pyramid
rows = int(input('Enter the number of rows:  '))
col = 2*rows-2
for i in range(rows,-1,-1):
    for j in range(col,0,-1):
        print(end=" ")
    col +=1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")