
# My 4 Favorite Python 3.14 Features
#1. F-Strings Debugging
#2. Improved Error Messages
#3. Template string literals
#4. Allow except and except* expressions


#1
# New: f"{var=}" prints name + value
name = "Chandra"
age = 25
print(f"Old way: Name={name}, Age={age}")
print(f"3.14 way: {name=}, {age=}")

#2
# New: Clearer hints (e.g., 'Did you mean?')

# Ex1: Typo (3.14 suggests close matches)
prin("Hello")

# Ex2: Undefined variable (clearer traceback)
x = 5
print(y)

# Correct version
print("Hello, Python 3.14!")  # Works fine
y = 10
print("Y value:", y)

