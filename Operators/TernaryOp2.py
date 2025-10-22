#Python program to implement ternary operator

a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
res=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All r Equal"
print("Max of ({},{},{})={}".format(a,b,c,res))