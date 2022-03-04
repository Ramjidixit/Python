#to calculate basic salary of employee
x=int(input('enter the basic salary: '))
if(x<10000):
 hra=(80*x)/100
 da=(90*x)/100
 print('the total salary=',x+hra+da)
elif(10000<x<=20000):
 hra=(85*x)/100
 da=(90*x)/100
 print('the total salary=',x+hra+da)
else:
 hra=(95*x)/100
 da=(95*x)/100
 print('the total salary=',x+hra+da)