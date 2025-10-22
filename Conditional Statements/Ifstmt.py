#Python program to implement simple if stmt

value=input("Enter value:")
if(value==value[::-1]):
    print("{} is Polindrome: ".format(value))
if(value!=value[::-1]):
    print("{} is not polindrome: ".format(value))
