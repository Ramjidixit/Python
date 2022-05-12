"""Write a program to add the sum of digits from 1 to 25, 50 to 76 and 90 to 101 using three
different for loops."""
def add(x,y):
    sum=0
    for i in range(x,y):
        sum=sum+i
    print("The sum of numbers from",x,"to",y,"is:",sum)
add(1,25)
add(50,76)
add(90,101)
