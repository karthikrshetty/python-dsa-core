"""
integers.py

This module demonstrates basic operations, properties, and usage of integers in Python.
"""

# Integer Declaration
a = 10
b = -5
c = 0

print("Integer values:", a, b, c)

# Type Checking
print("Type of a:", type(a))  # <class 'int'>

# Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (float):", a / 3)
print("Division (floor):", a // 3)
print("Modulus:", a % 3)
print("Exponentiation:", a ** 2)

# Comparison Operations
print("a > b:", a > b)
print("a == c:", a == c)
print("b < c:", b < c)

# Useful Built-in Functions
print("Absolute value of b:", abs(b))
print("Power (pow):", pow(a, 2))        # Same as a ** 2
print("Max and Min:", max(a, b, c), min(a, b, c))
print("Binary representation of a:", bin(a))  # '0b1010'
print("Hexadecimal representation of a:", hex(a))  # '0xa'
print("Octal representation of a:", oct(a))  # '0o12'
print("Integer from string:", int("42"))  # Converts string to integer
print("Integer from float:", int(3.99))  # Converts float to integer (truncates)
print("Integer from binary string:", int("1010", 2))  # Converts binary string to integer
print("Integer from hexadecimal string:", int("a", 16))  # Converts hex string to integer
print("Integer from octal string:", int("12", 8))  # Converts octal string to integer
print("Integer from float string:", int(float("3.14")))  # Converts float string to integer
print("Integer from boolean:", int(True))  # Converts boolean to integer (1)
print("Integer from boolean:", int(False))  # Converts boolean to integer (0)
# print("Integer from complex number:", int(3 + 4j))  # Raises ValueError