#python program to find biggest in two numbers
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
if(a>b):
    print("Biggest of {} and {}={}".format(a,b,a))
if(b>a):
    print("Biggest of {} and {}={}".format(a, b, b))
if(a==b):
    print("Both are equal")