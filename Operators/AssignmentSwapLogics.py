#Python program to implement Swapping of two numbers using assignment operators
a,b=input("Enter value of a: "),input("Enter value of b: ")
print("----------Swap logic 1-------")
print("----------Before Swap--------")
print("Original value of a={}".format(a))
print("Original value of b={}".format(b))

#Swap Logic using two variables
b,a=a,b
print("----------After Swap---------")
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))

print("\n")
print("----------Swap logic 2-------")
a,b=input("Enter value of a:"),input("Enter vaue of b: ")
print("----------Before Swap--------")
print("Original value of a={}".format(a))
print("Original value of b={}".format(b))

#Swap Logic using third variable
t=a
a=b
b=t
print("----------After Swap---------")
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))

print("\n")
print("----------Swap logic 3-------")
a,b=int(input("Enter value of a:")),int(input("Enter value of b: "))
print("----------Before Swap--------")
print("Original value of a={}".format(a))
print("Original value of b={}".format(b))

#Swap Logic without using third variable
a=a+b
b=a-b
a=a-b
print("----------After Swap---------")
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))

print("\n")
print("----------Swap logic 4-------")
a,b=int(input("Enter value of a:")),int(input("Enter value of b: "))
print("----------Before Swap--------")
print("Original value of a={}".format(a))
print("Original value of b={}".format(b))

#Swap Logic using floor Division ( // )
a=a*b
b=a//b
a=a//b
print("----------After Swap---------")
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))

print("\n")
print("----------Swap logic 5-------")
a,b=int(input("Enter value of a:")),int(input("Enter value of b: "))
print("----------Before Swap--------")
print("Original value of a={}".format(a))
print("Original value of b={}".format(b))

#Swapping Logic by using Bitwise XOR ( ^ )
a=a^b
b=a^b
a=a^b
print("----------After Swap---------")
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))