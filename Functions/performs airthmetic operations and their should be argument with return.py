#create a function which performs airthmetic operations and their should be argument with return.

def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a//b
    return c,d,e,f
x=int(input())
y=int(input())
n,n1,n2,n3=cal(x,y) 
print(n,n1,n2,n3)
    

 
