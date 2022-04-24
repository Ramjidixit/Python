"""Write a function to convert a number entered by the user into its corresponding number in words. 
For example, if the input is 876 then the output should be ‘Eight Seven Six’."""

def convert(num):
    numberNames = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',\
    5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    result = ''
    for ch in num:
        key = int(ch) #converts character to integer
        value = numberNames[key]
        result = result + ' ' + value
    return result
num = input("Enter any number: ")         #number is stored as string
result = convert(num)
print("The number is:",num)
print("The numberName is:",result)