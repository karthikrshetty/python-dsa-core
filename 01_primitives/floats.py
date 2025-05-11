"""
floats.py

Demonstrates basic usage and operations of floating-point numbers in Python.
"""

# Declaration
x = 10.5
y = -3.2
z = 0.0

print("Float values:", x, y, z)

# Type checking
print("Type of x:", type(x))  # <class 'float'>

# Arithmetic operations
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / 2)

# Rounding and precision
print("Rounded x:", round(x))
print("Rounded y (1 decimal):", round(y, 1))

# Type conversion
int_x = int(x)
print("Float to int:", int_x)

# Special float values
print("Infinity:", float('inf'))
print("Not a Number (NaN):", float('nan'))
# Comparison operations
print("x > y:", x > y)
print("x == z:", x == z)
print("y < z:", y < z)
# Useful built-in functions
print("Absolute value of y:", abs(y))
print("Power (pow):", pow(x, 2))  # Same as x ** 2
print("Max and Min:", max(x, y, z), min(x, y, z))
print("Binary representation of x:", bin(int(x)))  # '0b1010'
print("Hexadecimal representation of x:", hex(int(x)))  # '0xa'
print("Octal representation of x:", oct(int(x)))  # '0o12'
print("Float from string:", float("3.14"))  # Converts string to float
print("Float from integer:", float(42))  # Converts integer to float
print("Float from boolean:", float(True))  # Converts boolean to float (1.0)
print("Float from boolean:", float(False))  # Converts boolean to float (0.0)
# print("Float from complex number:", float(3 + 4j))  # Raises ValueError       