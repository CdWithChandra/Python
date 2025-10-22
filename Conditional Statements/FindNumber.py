#python program to find given number is +ve or -ve or 0

n=int(input("Enter number: "))
if(n>0):
    print("Number {} is +ve: ".format(n))
if(n<0):
    print("Number {} is -ve: ".format(n))
if(n==0):
    print("Number {} is 0: ".format(n))