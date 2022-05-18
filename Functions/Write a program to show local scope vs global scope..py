#Write a program to show local scope vs global scope.
p=20      #global variable
def demo():
    q=40    #local variable
    print("The value of lcal variable is q=",q)
    #access global variable inside functions
    print("The value of local variable p=",p)
demo()
#access gloabl variable outside function
print("The value of local variable p=",p)
"""print("The value of lcal variable is q=",q)  
if you write this here it will definitely show error.The local variable ‘q’ is defined 
within the function Demo(). The variable ‘q’ is accessed
from the function Demo(). The scope of a local variable lies within the block of the function, i.e. it
starts from its creation and continues up to the end of the function. Therefore, any attempt to access
the variable from outside of the function causes an error."""