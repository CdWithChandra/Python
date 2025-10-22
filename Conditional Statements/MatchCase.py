#Python program for match case
import sys

ch=int(input("Enter your choice: "))
match ch:
    case 1:
        print("-----------Addition-----------")
        a=float(input("Enter first value: "))
        b=float(input("Enter second value: "))
        print("Sum of ({},{})={}".format(a,b,a+b))
    case 2:
        print("-----------Substraction-----------")
        a=float(input("Enter first value: "))
        b=float(input("Enter second value: "))
        print("Sub of ({},{})={}".format(a,b,a-b))
    case 3:
        print("-----------Multiplication-----------")
        a=float(input("Enter first value: "))
        b=float(input("Enter second value: "))
        print("Multiple of ({},{})={}".format(a,b,a*b))
    case 4:
        print("-----Force exit program---------")
        sys.exit()

    case _:
        print("Select desired option: ")
print("Match case completed: ")