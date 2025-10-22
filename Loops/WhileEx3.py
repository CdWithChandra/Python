#python program to generate/print all even numbers 1 to n
n=int(input("Enter value/number to generate even numbers: "))
if n<=0:
    print("invalid input:")
else:
    print(" Numbers within {}:".format(n))
    i=2
    while i<=n:
        print("\t{}".format(i))
        i+=2
    else:
        print("--While else--")
print("Program complete")


