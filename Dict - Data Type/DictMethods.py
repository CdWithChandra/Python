# Python Dictionaries for Beginners
student={'name':'Chandra','age':25}
print(student.get('grade','Not found'))

student.update({'city': 'Bangalore', 'course': 'DevOps'})
print(student)

age = student.pop('age')
print(f"Removed: {age}")

print(student)
print(student.keys())

print(student.values())