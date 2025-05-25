"""
sets.py

Demonstrates set operations and methods.
"""

# Declaration
a = {1, 2, 3}
b = {3, 4, 5}
c = set()

# Add and Remove
a.add(4)
a.discard(2)
a.remove(1)
popped = a.pop()

# Set operations
union = a.union(b)
intersection = a.intersection(b)
difference = a.difference(b)
symmetric_diff = a.symmetric_difference(b)

# Checks
issubset = {3, 4}.issubset(b)
issuperset = b.issuperset({4})
isdisjoint = a.isdisjoint({10, 11})

# Update methods
d = {7, 8}
d.update({9})
d.intersection_update({8, 9})
d.difference_update({8})
d.symmetric_difference_update({9, 10})

# Built-ins
print("Length:", len(a))
print("Max:", max(b))
print("Min:", min(b))
print("All positive?", all(x > 0 for x in b))
print("Any even?", any(x % 2 == 0 for x in b))
print("Sorted:", sorted(b))
print("Set comprehension:", {x * 2 for x in b if x > 4})
print("Set comprehension with condition:", {x * 2 for x in b if x > 4})
print("Set comprehension with nested loop:", {(x, y) for x in b for y in a if x > 4})
print("Set comprehension with nested loop and condition:", {(x, y) for x in b for y in a if x > 4 and y > 2})
print("Set with mixed types:", {1, "apple", 3.14, True})
print("Set with nested sets:", {{1, 2}, {3, 4}, {5, 6}})
# Set as dictionary keys
set_key = frozenset({1, 2})
dictionary = {set_key: "value"}
print("Dictionary with set key:", dictionary)
# Set as set elements
set_set = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
print("Set with sets:", set_set)
# Set with named elements (using namedtuple)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print("Named set:", point)
# Set with default values (using namedtuple)
PointWithDefault = namedtuple('PointWithDefault', ['x', 'y'])
point_with_default = PointWithDefault(10, 20)
print("Named set with default values:", point_with_default)
# Set with variable-length arguments (using *args)
def variable_length_set(*args):
    return set(args)
variable_set = variable_length_set(1, 2, 3, 4)
print("Variable-length set:", variable_set)
# Set with frozen elements
frozen_set = frozenset({1, 2, 3})
print("Frozen set:", frozen_set)
# Set with mutable elements (not allowed)
# mutable_set = {1, [2, 3]}  # Raises TypeError
# Set with empty elements
empty_set = set()
print("Empty set:", empty_set)
# Set with empty frozenset
empty_frozenset = frozenset()
print("Empty frozenset:", empty_frozenset)
# Set with empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)
# Set with empty list
empty_list = []
print("Empty list:", empty_list)
# Set with empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)
# Set with empty bytearray
empty_bytearray = bytearray()
print("Empty bytearray:", empty_bytearray)
# Set with empty bytes
empty_bytes = b''
print("Empty bytes:", empty_bytes)
# Set with empty string
empty_string = ""
print("Empty string:", empty_string)
