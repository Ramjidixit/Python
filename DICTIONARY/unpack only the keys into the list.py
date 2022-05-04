"""unpack only the keys into the list"""

a={"ram":89,"raj":78,"poju":74}
b={"rajeev":58,"poi":82,"hjiu":56}
c={"pooja":75,"parth":49,"vijay":79}
d=list({*a,*b,*c})
print(d)