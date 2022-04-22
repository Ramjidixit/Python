'''wap to find the maximum marks from the following dictionary {"ram":55,"madhav":87,"raman":45} 
and also find the name of student'''

d={"ram":55,"madhav":87,"raman":45}
maxx=0
for i in d:
    if d[i]>maxx:
        maxx=d[i]
        name=i
print("The highest marks is of :",name,"which are=",maxx)
