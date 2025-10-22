#Simple If Else program

a=int(input("Enter first number: "))
b=int(input("Enter first number: "))
if(a>b):
    print("Max of({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("Max of({},{})={}".format(a, b, b))
    else:
        print("Both Values are equal")
    print("Iam else part ")
print("I am from if part")