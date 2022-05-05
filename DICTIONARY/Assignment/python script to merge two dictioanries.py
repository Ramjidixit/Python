#write a python script to merge two dictioanries.
a={"hare":78,"krishna":85,"ram":82}
b={"parth":56,"rinku":28,"vijay":99}
c={}
c={**a,**b}
print(c)