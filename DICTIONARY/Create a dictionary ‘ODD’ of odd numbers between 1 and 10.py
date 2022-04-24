"""Create a dictionary ‘ODD’ of odd numbers between 1 and 10, where the key is the decimal number and
the value is the corresponding number in words. Perform the following operations
on this dictionary:
(a) Display the keys
(b) Display the values
(c) Display the items
(d) Find the length of the dictionary
(e) Check if 7 is present or not
(f) Check if 2 is present or not
(g) Retrieve the value corresponding to the key 9
(h) Delete the item from the dictionary corresponding to the key 9"""

s={1:"one",3:"three",5:"five",7:"seven",9:"nine"}
print(s.keys())
print(s.values())
print(s.items())
print(len(s))
print(7 in s)
print(2 in s)
print(s[9])
del s[9]
print(s)
