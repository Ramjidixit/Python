"""wap to ask the records of n student.each record contains name of student,roll number and marks of 3 subjects.
like[2101,"rahul",85,45,63]. create a dictioanry where the roll number acting as keys and total marks acting 
as values and then find the student roll number who has highest marks."""

d={}
n=int(input("Enter the total number of students:"))
for i in range(n):
    r=int(input("Enter the roll number:"))
    n=input("Enter the name:")
    print("Enter the marks of 3 subject:")
    a=int(input())
    b=int(input())
    c=int(input())
    d[r]=[n,a+b+c]
print(d) #this dictionary shows roll number as key and name and total marks as value.
p=max(d,key=d.get)
print("The highest marks of:",p)