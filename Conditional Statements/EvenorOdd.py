#python program to find even or odd only + number

n=int(input("Enter number: "))
if(n>0) and (n%2==0):
    print("Given number {} is Even:".format(n))
if(n>0) and (n%2!=0):
    print("Given number {} is Odd:".format(n))
if(n<0):
    print("Invalid input")