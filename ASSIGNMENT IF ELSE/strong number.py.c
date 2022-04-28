#check whether the given number is strong number or not.

n=int(input("enter the number:"))
d=0
for a in range(1,n):
 if n%a==0:
  d=d+a
if d==n:
 print("yes")
else:
 print("not")