#python program to read 2 numerical values and find their product/sum
from sys import float_repr_style

a=float(input("Enter first value: "))
b=float(input("Enter second value: "))
c=a+b
print("---------Product/Sum-----------")
print("Value of a={}".format(a))
print("Value of b={}".format(b))
print("Sum of({},{})={}".format(a,b,c))
print("---------Another way Product/Sum-----------")
print("Value of a={}".format(a))
print("Value of b={}".format(b))
print(f"Product({a},{b})={a*b}")
print("---------Another way Product/Sum-----------")
print("Product=",float(input("Enter first value: "))*float(input("Enter second value:")))
