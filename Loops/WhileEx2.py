#python program to generate/print 1 to n numbers in reverse

n=int(input("Enter value: "))
if n<=0:
    print("Invalid Number ")
else:
    print(" Numbers from {} to 1: ".format(n))
   # i=1  initialisation part
    while n>=0:  #condition
        print("\t {}".format(n))
        n-=1 #updation
    else:
        print("---While else part---")



