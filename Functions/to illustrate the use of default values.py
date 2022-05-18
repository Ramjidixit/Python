#Write a program to illustrate the use of default values in a function’s definition.
def raj(name,msg="welcome to python programming."):
    print("hello",name,msg)
raj("sachin")

"""If a value is provided, it will overwrite the default value"""