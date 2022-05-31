#to access items 
a=['ram','raj','radha','rajeev','riya','raju']
print(a[2]) #to print by giving index
print(a[-3])
#print(a[-9]) #out of range so give error
print(a[1:4]) #to print in range
print(a[2:5]) #to print second,thrd and fourth element
#to print till rajeev but not including rajeev 
print(a[:3])
print(a[0:]) #to print from starting to last 
print(a[-3:-1]) #it print till riya excluding raju

#to check items exist or not 
if "raj" in a:
    print("yes ,it is here")

