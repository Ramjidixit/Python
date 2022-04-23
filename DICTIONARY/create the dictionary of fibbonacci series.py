"""wap to input the value of n and then create the dictionary of fibbonacci series 
{1:0,2:1,3:1,4:2,5:3,6:5,7:8..................}"""

d={1:0,2:1}
n=int(input("Enter the number:"))
a=0
b=1 
sum=0
count=3
print("Fibonacci series:",end="")
while count<=n:
    sum=a+b
    d[count]=sum 
    count+=1 
    a=b
    b=sum
print(d)