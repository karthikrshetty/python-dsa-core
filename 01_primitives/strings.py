"""
strings.py

Demonstrates string creation, manipulation, and common methods in Python.
"""

# Declaration
s1 = "Hello"
s2 = 'World'
s3 = ""

print("String values:", s1, s2)

# Type checking
print("Type of s1:", type(s1))  # <class 'str'>

# Concatenation and repetition
print("Concatenation:", s1 + " " + s2)
print("Repetition:", s1 * 3)

# Indexing and slicing
print("First character:", s1[0])
print("Last character:", s1[-1])
print("Substring:", s1[1:4])

# String methods
print("Uppercase:", s1.upper())
print("Lowercase:", s2.lower())
print("Is alpha:", s1.isalpha())
print("Length of s1:", len(s1))

# String formatting
name = "Alice"
age = 25
print(f"{name} is {age} years old.")

# Escape characters
print("Line break:\nNew line here.")
print("Tab space:\tAfter tab.")
print("Backslash: \\")
print("Single quote: \'")
print("Double quote: \"")
print("Raw string: r'\\n'")
print("Raw string with escape: r'\\n' and 'Hello'")