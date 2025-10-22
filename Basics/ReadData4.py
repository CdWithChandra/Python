#Pythong program to read date from the keyboard
a=float(input("Enter a value: "))
print(a,type(a))
print("----------Int Data Type-----------")
a=int(input("Enter int value: "))
print(a,type(a))
print("----------Bool Data Type-----------")
a=bool(input("Enter int value: "))
print(a,type(a))
print("----------Range Data Type-----------")
a=range(10,21,2)
for v in a:
    print(v)
    print("----------Using Enumerate-----------")
for x, v in enumerate(a):
    print(x,"-->",v,"-->",type(v))