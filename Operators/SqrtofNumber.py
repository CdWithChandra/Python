#Python program to calculate square root of a number using math function
import math

a=float(input("Enter a number: "))
sqrt=math.sqrt(a)
print("---------Square root with math module----------")
print("Square root of a {}={} ".format(a,sqrt))
print("---------Square root without math module----------")
sqrt=a**0.5
print("Square root of a {}={} ".format(a,sqrt))
