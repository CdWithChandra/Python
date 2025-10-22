#print message
from token import STRING
from traceback import print_tb

a=10
b=20
c=a+b
print("Hello Python World")
print("Hello", "Python", "World")
print("Hello"+"Python"+"Wprld")
print("Hello"+" "+"Python"+" "+"World")
print("Python3.13")
print("Python"+str(3.13))
print("Sum of",a,"and",b,"=",c)
print("Sum of "+str(a)+" and "+str(b)+"="+str(c) )
print("sum(",a,",",b,")=",c)
print("sum("+str(a)+","+str(b)+")="+str(c))

print("Value of a=",a)
print("Value of a="+str(a))
print("Value of a={}".format(a))
print("Sum={}".format(c))
print("Sum of {} and {}={}".format(a,b,c))
print("{}+{}={}".format(a,b,c))


