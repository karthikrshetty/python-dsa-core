"""
lists.py

Comprehensive demonstration of list creation and all major built-in methods in Python.
"""

# Declaration
fruits = ["apple", "banana", "cherry"]
numbers = [3, 1, 4, 1, 5]

# Access and modify
print(fruits[0])
fruits[1] = "mango"

# List methods
fruits.append("orange")
fruits.insert(1, "grape")
fruits.extend(["kiwi", "melon"])
fruits.remove("apple")
popped = fruits.pop()  # removes last item
count = fruits.count("mango")
index = fruits.index("mango")
fruits.reverse()
fruits.sort()

print("Modified fruits:", fruits)
print("Popped:", popped)
print("Count of 'mango':", count)
print("Index of 'mango':", index)

# Other built-ins
print("Length:", len(fruits))
print("Max number:", max(numbers))
print("Min number:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted (new):", sorted(numbers))
print("Any > 4:", any(x > 4 for x in numbers))
print("All > 0:", all(x > 0 for x in numbers))
print("Enumerate:", list(enumerate(fruits)))
print("List comprehension:", [x for x in numbers if x > 2])
print("List comprehension with condition:", [x * 2 for x in numbers if x > 2])
print("List comprehension with if-else:", [x * 2 if x > 2 else x for x in numbers])
print("List comprehension with nested loop:", [(x, y) for x in numbers for y in fruits if x > 2])
print("List comprehension with nested loop and condition:", [(x, y) for x in numbers for y in fruits if x > 2 and y.startswith('m')])
