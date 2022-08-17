"""Write a program to read the weight of an object in grams and display its weight in kilograms
and grams, respectively."""
g=eval(input("Enter the weight in grams:"))
k=g//1000
l=g-(k*1000)
print("The weight=",k,"kg",l,"grams")