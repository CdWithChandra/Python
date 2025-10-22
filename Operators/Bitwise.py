#Python program to implement identity operators

lst1=[10,"RS",23.44]
print(lst1,type(lst1),id(lst1))
lst2=lst1
print(lst2,type(lst2),id(lst2))

#Deep copy
print("\n -----Check Identity operator-----")
print(lst1 is lst2)
print(lst2 is lst1)
print(lst1 is not lst2)
print(lst2 is not lst1)

#Shallow copy
lst2=lst1.copy()
print(lst1,id(lst1))
print(lst2,id(lst2))
print("\n -----Check Identity operator-----")
print(lst1 is lst2)
print(lst2 is lst1)
print(lst1 is not lst2)
print(lst2 is not lst1)

a=None
b=None
print(a,id(a))
print(b,id(b))
print("\n -----Check Identity operator-----")
print(a is b)
print(b is a)
print(a is not b)
print(b is not a)