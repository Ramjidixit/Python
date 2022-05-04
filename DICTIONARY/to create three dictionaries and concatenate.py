"""Write a program to create three dictionaries and concatenate them to
create fourth dictionary."""
a={"ram":89,"raj":78,"poju":74}
b={"rajeev":58,"poi":82,"hjiu":56}
c={"pooja":75,"parth":49,"vijay":79}
e={}
for f in (a,b,c):
    e.update(f)
print(e)

#one more way of doing 
g={**a,**b,**c}
print(g)