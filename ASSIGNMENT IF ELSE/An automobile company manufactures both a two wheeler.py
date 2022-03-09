"""An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:
•	1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
•	2nd data, Total number of wheels = W
The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.
Example :
Input :
•	200  -> Value of V
•	540   -> Value of W
Output :
•	TW =130 FW=70"""

v=int(input("Enter the number of vehicle:"))
w=int(input("Enter total number of wheels:"))
print("TW=",((-w+(4*v))//2),"FW=",(w-(2*v))//2)
