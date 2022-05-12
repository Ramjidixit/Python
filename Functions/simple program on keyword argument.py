"""keyword argument-An alternative to positional argument is keyword argument. If a programmer knows the parameter
name used within the function then he/she can explicitly use the parameter name while calling the
function. A programmer can pass a keyword argument to a function by using its corresponding
parameter name rather than its position"""

#Write a simple program on keyword argument
def Display(Name,age):
    print("Name = ",Name,"age = ",age)
Display(age=25,Name="John")