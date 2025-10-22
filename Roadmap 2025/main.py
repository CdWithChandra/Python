#----------------------------------
#  Python - Roadmap 2025
#----------------------------------
from multiprocessing.managers import convert_to_error

#1 No variable should be taken as a keywords
#2 variable name should be a combination of alphabets, numbers, _
#3 Within variable name no special symbols are allowed (except _)
#4 First letter of variable name start with either alphabet or _
# all the variables are case sensitive in python

a=12
age=23
name="chandra"
print(a)
print(age)
print(name)

# variables, data types, Strings
age=25 # int
height=5.9 # float
name="chandra" # string
is_programmer=True #bool

message=name+""+"PYTHON"
print(message)

name="chandra"
print(name.upper())
print(len(name))
print(name.strip())
print(message.strip())

# list, Tuple , Dict, Set

lst=[1,2,3,4]
print(lst)
lst.append(5)
print(lst)

tpl=(1,2,3,4)
print(tpl,id(tpl))

stu={"name": "Bandan","age":25,"grade":"A"}
print(stu)

print(stu['name'])
print(stu['age'])
print(stu['grade'])

numbers={1,2,2,3,4,4,5}
print(numbers)

str={"name","chandra","name"}
print(str)

# loops & conditionals

age=18
if age>=18:
    print("will not allowed to watch movies ")
else:
    print("Allowed to watch movie")

for i, v in enumerate(range(6)):
    print(i, v)

count=0
while count<5:
    print("Count is:",count)
    count +=1

# functions and scopes
def greeting(name):
    return "Hello"+name
print(greeting("chandra"))

x=10  # global to function
def my_Function():
    x=5   # local to function
    print("inside funtion:", x)
my_Function()
print("Outside function:",x)

# Class and object
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

        def greet(self):
            print(f"hello, My name is {self.name} and I am {self.age} years old")

s1=Person("chandra",25)
print(s1.age)
print(s1.name)

# File operations

with open("example.txt","w") as file:
    file.write("Hello, Python!\n")

with open("example.txt","r") as file:
    content=file.read()
    print(content)

