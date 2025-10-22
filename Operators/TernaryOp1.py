#Python program to implement ternary operator

a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
res=a if a>b else b
print("Max({},{})={}".format(a,b,res))

print("-----------Another way------")
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
res=b if b>a else a
print("Max({},{})={}".format(a,b,res))

print("-----------Another way------")
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
res=a if a>b else b if b>a else "Both are equal"
print("Max({},{})={}".format(a,b,res))
