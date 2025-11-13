
# What is a lambda function?

# Key terms
# Lambda
# any no of args
# short and simple functions we use

add_10=lambda x: x+10
print("lamdna",add_10(5))

multiply=lambda x,y:x*y
print("multiply", multiply(2,5))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("squeares",squares)