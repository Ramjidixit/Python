'''Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and 
	Computer. Calculate percentage and grade according to following: 
	Percentage >= 90% : Grade A 
	Percentage >= 80% : Grade B 
	Percentage >= 70% : Grade C 
	Percentage >= 60% : Grade D 
	Percentage >= 40% : Grade E 
	Percentage < 40% : Grade F''' 
a=int(input("Enter the marks of physics:"))
b=int(input("Enter the marks of chemistry:"))
c=int(input("Enter the marks of biology:"))
d=int(input("Enter the marks of mathematics:"))
e=int(input("Enter the marks of Computer:"))
p=(a+b+c+d+e)*100
r=p/500
print("percentage=",r)
if(r>=90):
    print("Grade A")
elif(r>=80):
    print("Grade B")
elif(r>=70):
    print("Grade c")
elif(r>=60):
    print("Grade D")
elif(r>=40):
    print("Grade E")
else:
    print("Grade F")
