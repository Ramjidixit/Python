"""write a program to assign grades to students and display all the grades using keys() and get() 
method of a dictioanry"""

grades={"tamanna":"a","yash":"b","raj":"c"}
for key in grades.keys():
    print(key,"",grades.get(key,0))