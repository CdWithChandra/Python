#python program for multiplication table of given number
n=int(input("Enter value/number to generate even numbers: "))
if n<=0:
    print("Invalid")
else:
    print(" Multiplication table for {}".format(n))
    i=1
    while i<=10:
        print(" {}*{}={}".format(n,i,n*i))
        i=i+1
    else:
        print(" Else")

