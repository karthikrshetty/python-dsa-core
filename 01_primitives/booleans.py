"""
booleans.py

Demonstrates Boolean data type operations and logical expressions in Python.
"""

# Declaration
a = True
b = False

print("Boolean values:", a, b)

# Type checking
print("Type of a:", type(a))  # <class 'bool'>

# Logical operations
print("AND:", a and b)
print("OR:", a or b)
print("NOT a:", not a)

# Comparison expressions return booleans
x = 5
y = 10
print("x < y:", x < y)
print("x == y:", x == y)

# Boolean as integers
print("True as int:", int(True))   # 1
print("False as int:", int(False)) # 0
# Boolean from integers
print("Boolean from 1:", bool(1))   # True
print("Boolean from 0:", bool(0))   # False
print("Boolean from non-zero int:", bool(42))  # True
print("Boolean from empty string:", bool(""))  # False
print("Boolean from non-empty string:", bool("Hello"))  # True
print("Boolean from empty list:", bool([]))  # False
print("Boolean from non-empty list:", bool([1, 2, 3]))  # True
print("Boolean from None:", bool(None))  # False
# Boolean from complex number
# print("Boolean from complex number:", bool(3 + 4j))  # True
# Boolean from float
print("Boolean from float 0.0:", bool(0.0))  # False
print("Boolean from float 3.14:", bool(3.14))  # True
# Boolean from NaN
print("Boolean from NaN:", bool(float('nan')))  # True
# Boolean from infinity
print("Boolean from infinity:", bool(float('inf')))  # True
# Boolean from empty dictionary
print("Boolean from empty dict:", bool({}))  # False
print("Boolean from non-empty dictionary:", bool({"key": "value"}))  # True
# Boolean from empty set
print("Boolean from empty set:", bool(set()))  # False
print("Boolean from non-empty set:", bool({1, 2, 3}))  # True
# Boolean from empty tuple
print("Boolean from empty tuple:", bool(()))  # False
print("Boolean from non-empty tuple:", bool((1, 2, 3)))  # True
# Boolean from frozenset
print("Boolean from empty frozenset:", bool(frozenset()))  # False
print("Boolean from non-empty frozenset:", bool(frozenset({1, 2, 3})))  # True
# Boolean from bytearray
print("Boolean from empty bytearray:", bool(bytearray()))  # False
print("Boolean from non-empty bytearray:", bool(bytearray([1, 2, 3])))  # True
# Boolean from bytes
print("Boolean from empty bytes:", bool(b''))  # False
print("Boolean from non-empty bytes:", bool(b'Hello'))  # True
# Boolean from memoryview
print("Boolean from empty memoryview:", bool(memoryview(b'')))  # False
print("Boolean from non-empty memoryview:", bool(memoryview(b'Hello')))  # True