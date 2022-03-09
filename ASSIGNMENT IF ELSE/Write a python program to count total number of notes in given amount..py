#Write a C program to count total number of notes in given amount. 
a=int(input("Enter the total amount:"))
b=a//2000
#b is the notes of 2000
c=(a-(2000*b))//500
#c is the number of notes of 500
d=(500*c)+(2000*b)
e=(a-d)//200
#e is the notes of 200
f=(200*e)+d
g=(a-f)//100
# g is the notes of 100
h=(100*g)+f
i=(a-h)//50
# i is the notes of 50
j=(50*i)+h
k=(a-j)//20
#k is the notes of 20
l=(20*k)+j 
m=(a-l)//10 
print("number of notes of 2000=",b)
print("number of notes of 500=",c)
print("number of notes of 200=",e)
print("number of notes of 100=",g)
print("number of notes of 50=",i)
print("number of notes of 20=",k)
print("number of notes of 10=",m)
print("The total number of notes=",b+c+e+g+i+k+m)