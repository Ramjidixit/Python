"""create the following dictionary:
{"A":a,"B":b,"C":c,..................,"Z":z}"""
d={}
import string 
for letter in string.ascii_uppercase:
    d[letter]=letter.lower()
print(d)
