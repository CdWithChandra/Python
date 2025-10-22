#Python program to implement Arithmetic operators
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))

print("-"*10,"Arithmetic Operations","-"*10)
print("Sum of ({},{})={}".format(a,b,a+b))
print("Subtract of ({},{})={}".format(a,b,a-b))
print("Multiple of ({},{})={}".format(a,b,a*b))
print("Division of ({},{})={}".format(a,b,a/b))
print("Floor Division of ({},{})={}".format(a,b,a//b))
print("Modular/Reminder of ({},{})={}".format(a,b,a%b))
print("Power of ({},{})={}".format(a,b,a**b))