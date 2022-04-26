"""wap to create the following dictionary:
{"A":65,"B":66,"C":67,................,"Z":90,"a":97,"b":98,............,"z":122}"""
import string 
d={}
for letter in string.ascii_uppercase:
    d[letter]=ord(letter) 
for letter in string.ascii_lowercase:
    d[letter]=ord(letter)
print(d)