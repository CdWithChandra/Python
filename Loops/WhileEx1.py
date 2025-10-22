#python program to generate/print 1 to n numbers
from traceback import print_tb

n=int(input("Enter number: "))
if n<=0:
    print("Invalid number: ")
else:
    print("Numbers witin: {}".format(n))
    i=1 #Intialisation part
    while i<=n: #condition part
        print("\t {}".format(i))
        i=i+1 #update part
    else:
      print("---While completed---")
    print("--else completed---")

