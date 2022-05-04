#write a python script to merge two dictionaries.
a={"raj":78,"rahul":45,"shreya":85,"prachi":52}
b={"happy":56,"sad":82,"hello":93}
c={}
c={**a,**b}
print(c)