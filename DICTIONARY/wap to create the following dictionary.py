"""wap to create the following dictionary:
{"A":65,"B":66,"C":67,................,"Z":90}"""

import string
d={}
for letter in string.ascii_uppercase:
    d[letter]=ord(letter)
print(d)