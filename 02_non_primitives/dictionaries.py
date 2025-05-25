"""
dictionaries.py

Demonstrates all major dictionary methods and functions.
"""

# Declaration
student = {"name": "Alice", "age": 21, "grade": "A"}

# Access & modify
print(student["name"])
student["age"] = 22
student["email"] = "alice@example.com"

# Dictionary methods
print("Get with default:", student.get("address", "N/A"))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Pop 'grade':", student.pop("grade"))
print("Popitem:", student.popitem())  # removes last key-value pair
student.update({"city": "Delhi", "email": "new@example.com"})
print("After update:", student)

# From keys
defaults = dict.fromkeys(["a", "b", "c"], 0)

# Checks
print("Is 'name' in dict?", "name" in student)

# Built-in functions
print("Length:", len(student))
print("All values truthy?", all(student.values()))
print("Any key truthy?", any(student.keys()))
print("Sorted keys:", sorted(student.keys()))
print("Dictionary comprehension:", {k: v for k, v in student.items() if isinstance(v, str)})
print("Dictionary comprehension with condition:", {k: v for k, v in student.items() if isinstance(v, str)})
print("Dictionary comprehension with nested loop:", {k: v for k, v in student.items() if isinstance(v, str) and len(k) > 2})
print("Dictionary comprehension with nested loop and condition:", {k: v for k, v in student.items() if isinstance(v, str) and len(k) > 2})
print("Dictionary with mixed types:", {"name": "Alice", 1: [1, 2, 3], (1, 2): {1, 2}})
print("Dictionary with nested dictionaries:", {"student": {"name": "Alice", "age": 21}, "course": {"name": "Math", "code": 101}})
