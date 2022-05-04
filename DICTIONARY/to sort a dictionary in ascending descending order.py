"""Write a program to sort a dictionary in ascending/descending order by
key and ascending/descending order by value."""
a={"ram":56,"rahim":23,"piyush":59,"raju":85}
print("original dictionary:",a)
print(sorted (a.items()))  #to print in ascending order by key
print(sorted (a.items(),reverse=True))  #to print in descending order by key

