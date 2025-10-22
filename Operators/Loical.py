#Python program to implement logical operators

#
print("----------And Operator---------")
print("--------With True/False -------")
print(True and False)
print(True and True)
print(False and True)
print(False and False)

print("--------With Numbers-----------")
#With numbers
print(10 and 20)
print(20 and 10)
print(10>5 and 20>10)
print(10>20 and 30>20)
print(10>20 and 30>20 and 40>10)
print(10>5 and 20>30 and 40>20 and 20>-20)
print(100>50 and 200>20 and 400>30)

print("\n")
print("----------OR Operator------------")
print("--------With True/False -------")
print(True or False)
print(True or True)
print(False or True)
print(False or False)
print("--------With Numbers-----------")
print(100 or 200)
print(0 or 200)
print("Python" or "Java")

print(100 or 0 or 200)
print(10>2 or 20>30)
print(100>200 or 50>40)
print(10>2 or 40>30 or 50>30)
print( 10>20 or 30>40 or 50>60)

print("\n")
print("----------OR Operator------------")
print("--------With True/False -------")
print(not True)
print(not False)


