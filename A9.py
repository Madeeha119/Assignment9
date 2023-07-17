import math
import string 
# #predefined modules used below
k=77.7
print("Original value of K =",k)
print("Ciel = ",math.ceil(k))
print("Floor = ",math.floor(k))
m=25
print("Original value of M =",m)
print("Square root of M =",math.sqrt(m))
w=[1,2,3,4,5,6,7]
print("Elements present in W : ",w)
print("Sum of all elements in W = ",math.fsum(w))
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print("//Enter the Values for addition,subtraction,multiplication,division//")
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
print("Addition of A and B = ",(a+b))
print("Subtraction of A and B = ",(a-b))
print("Multiplication of A and B = ",(a*b))
print("Division of A and B = ",(a/b))  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print("// Strings Module Functions //") 

string_concat=20
x=input("\nEnter string1 : ")
y=input("Enter string2 : ")
x+=y
print("Concate string successfully...")
print("result = ",(x)) 

str="madeeha zardi"
#t=string_concat(x,y)
print("Converting into uppercase :",str.upper())
print("Converting into lowercase :",str.lower())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
names='madeeha siddhi drishti riya'
print("New String :",names)
print("Splitting a string when a space is detected...")
print(names.split())
