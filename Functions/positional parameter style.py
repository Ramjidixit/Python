"""positional argument style or positional parameter style:the first argument binds to
the first parameter and the second argument binds to the second parameter"""
def Display(Name,age):
    print("Name = ",Name,"age =",age)
Display("John",25)
Display(40,"Sachin")

"""this code print erroer:
def Display(Name,age):
    print(“Name = “,Name,”age = “,age)
Display(“John”)
because As the function call contains lesser number of arguments as compared to the
function definition, Python will report a missing argument error"