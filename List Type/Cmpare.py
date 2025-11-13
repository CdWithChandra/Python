# Lists vs Tuples
# Critical Differences & Dangerous
import datetime
import sys
import time

# DIFFERENCE #1 - MUTABILITY

#List
user_roles=['viewer','editor','admin']
user_roles[0]='super_admin'

#Tuple
user_roles=('viewer','editor','admin')


# DIFFERENCE #2 - MEMORY IMPACT

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"List: {sys.getsizeof(list_data)} bytes")
print(f"Tuple: {sys.getsizeof(tuple_data)} bytes")

# DIFFERENCE #3 - PERFORMANCE REALITY
permissions = ['read', 'write', 'admin']
start = time.time()
for _ in range(1000000):
    'admin' in permissions
list_time = time.time() - start

permissions = ('read', 'write', 'admin')
start = time.time()
for _ in range(1000000):
    'admin' in permissions
tuple_time = time.time() - start

print(f"List: {list_time:.3f}s")
print(f"Tuple: {tuple_time:.3f}s")
