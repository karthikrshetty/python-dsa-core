"""
tuples.py

Demonstrates tuple operations and built-in functions.
"""

# Declaration
data = (10, 20, 30, 20)
single = (5,)

# Access
print(data[0])
print("Slice:", data[1:3])

# Built-in methods
print("Count of 20:", data.count(20))
print("Index of 30:", data.index(30))

# Built-in functions
print("Length:", len(data))
print("Max:", max(data))
print("Min:", min(data))
print("Sum:", sum(data))

# Unpacking
a, b, c, d = data
print("Unpacked:", a, b, c, d)
# Tuple concatenation
new_data = data + single
print("Concatenated:", new_data)
# Tuple repetition
repeated = single * 3
print("Repeated:", repeated)
# Tuple comprehension (using generator expression)
comprehension = tuple(x * 2 for x in data)
print("Tuple comprehension:", comprehension)
# Tuple with mixed types
mixed = (1, "apple", 3.14, True)
print("Mixed tuple:", mixed)
# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
# Tuple as dictionary keys
tuple_key = (1, 2)
dictionary = {tuple_key: "value"}
print("Dictionary with tuple key:", dictionary)
# Tuple as set elements
tuple_set = {(1, 2), (3, 4), (5, 6)}
print("Set with tuples:", tuple_set)
# Tuple with named elements (using namedtuple)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print("Named tuple:", point)
# Tuple with default values (using namedtuple)
PointWithDefault = namedtuple('PointWithDefault', ['x', 'y'])
point_with_default = PointWithDefault(10, 20)
print("Named tuple with default values:", point_with_default)
# Tuple with variable-length arguments (using *args)
def variable_length_tuple(*args):
    return args
variable_tuple = variable_length_tuple(1, 2, 3, 4)
print("Variable-length tuple:", variable_tuple)
# Tuple with keyword arguments (using **kwargs)
def keyword_arguments_tuple(**kwargs):
    return kwargs
keyword_tuple = keyword_arguments_tuple(a=1, b=2, c=3)
print("Keyword arguments tuple:", keyword_tuple)
# Tuple with unpacking in function arguments
def unpacking_tuple(a, b, c):
    return a + b + c
unpacked_result = unpacking_tuple(*data)
print("Unpacking in function arguments:", unpacked_result)
# Tuple with unpacking in function return
def return_tuple():
    return 1, 2, 3
unpacked_result = return_tuple()
print("Unpacking in function return:", unpacked_result)
# Tuple with unpacking in list comprehension
list_comprehension = [x * 2 for x in data]
print("List comprehension with tuple unpacking:", list_comprehension)
# Tuple with unpacking in dictionary comprehension
dict_comprehension = {x: x * 2 for x in data}
print("Dictionary comprehension with tuple unpacking:", dict_comprehension)
# Tuple with unpacking in set comprehension
set_comprehension = {x * 2 for x in data}
print("Set comprehension with tuple unpacking:", set_comprehension)
# Tuple with unpacking in generator expression
generator_expression = (x * 2 for x in data)
print("Generator expression with tuple unpacking:", list(generator_expression))
# Tuple with unpacking in map function
map_result = tuple(map(lambda x: x * 2, data))
print("Map function with tuple unpacking:", map_result)
# Tuple with unpacking in filter function
filter_result = tuple(filter(lambda x: x > 20, data))
print("Filter function with tuple unpacking:", filter_result)
# Tuple with unpacking in reduce function
from functools import reduce
reduce_result = reduce(lambda x, y: x + y, data)
print("Reduce function with tuple unpacking:", reduce_result)
# Tuple with unpacking in zip function
zip_result = tuple(zip(data, single))
print("Zip function with tuple unpacking:", zip_result)
# Tuple with unpacking in all function
all_result = all(x > 0 for x in data)
print("All function with tuple unpacking:", all_result)
# Tuple with unpacking in any function
any_result = any(x > 20 for x in data)
print("Any function with tuple unpacking:", any_result)
# Tuple with unpacking in sorted function
sorted_result = tuple(sorted(data))
print("Sorted function with tuple unpacking:", sorted_result)
# Tuple with unpacking in reversed function
reversed_result = tuple(reversed(data))
print("Reversed function with tuple unpacking:", reversed_result)
# Tuple with unpacking in enumerate function
enumerate_result = tuple(enumerate(data))
print("Enumerate function with tuple unpacking:", enumerate_result)
# Tuple with unpacking in zip_longest function
from itertools import zip_longest
zip_longest_result = tuple(zip_longest(data, single))
print("Zip longest function with tuple unpacking:", zip_longest_result)
# Tuple with unpacking in combinations function
from itertools import combinations
combinations_result = tuple(combinations(data, 2))
print("Combinations function with tuple unpacking:", combinations_result)
# Tuple with unpacking in permutations function
from itertools import permutations
permutations_result = tuple(permutations(data, 2))
print("Permutations function with tuple unpacking:", permutations_result)
# Tuple with unpacking in product function
from itertools import product
product_result = tuple(product(data, single))
print("Product function with tuple unpacking:", product_result)
# Tuple with unpacking in chain function
from itertools import chain
chain_result = tuple(chain(data, single))
print("Chain function with tuple unpacking:", chain_result)
# Tuple with unpacking in cycle function
from itertools import cycle
cycle_result = tuple(next(cycle(data)) for _ in range(5))
print("Cycle function with tuple unpacking:", cycle_result)
# Tuple with unpacking in islice function
from itertools import islice
islice_result = tuple(islice(data, 2))
print("Islice function with tuple unpacking:", islice_result)
# Tuple with unpacking in tee function
from itertools import tee
tee_result = tuple(tee(data, 2))
print("Tee function with tuple unpacking:", tee_result)
# Tuple with unpacking in starmap function
from itertools import starmap
starmap_result = tuple(starmap(lambda x, y: x + y, zip(data, single)))
print("Starmap function with tuple unpacking:", starmap_result)
# Tuple with unpacking in accumulate function
from itertools import accumulate
accumulate_result = tuple(accumulate(data))
print("Accumulate function with tuple unpacking:", accumulate_result)
# Tuple with unpacking in groupby function
from itertools import groupby
groupby_result = tuple(groupby(data))
print("Groupby function with tuple unpacking:", groupby_result)
# Tuple with unpacking in combinations_with_replacement function
from itertools import combinations_with_replacement
combinations_with_replacement_result = tuple(combinations_with_replacement(data, 2))
print("Combinations with replacement function with tuple unpacking:", combinations_with_replacement_result)
# Tuple with unpacking in permutations_with_replacement function
from itertools import permutations_with_replacement
permutations_with_replacement_result = tuple(permutations_with_replacement(data, 2))
print("Permutations with replacement function with tuple unpacking:", permutations_with_replacement_result)
# Tuple with unpacking in product_with_replacement function
from itertools import product_with_replacement
product_with_replacement_result = tuple(product_with_replacement(data, single))
print("Product with replacement function with tuple unpacking:", product_with_replacement_result)
# Tuple with unpacking in combinations_with_replacement function
from itertools import combinations_with_replacement
combinations_with_replacement_result = tuple(combinations_with_replacement(data, 2))
print("Combinations with replacement function with tuple unpacking:", combinations_with_replacement_result)
# Tuple with unpacking in permutations_with_replacement function
from itertools import permutations_with_replacement
permutations_with_replacement_result = tuple(permutations_with_replacement(data, 2))
print("Permutations with replacement function with tuple unpacking:", permutations_with_replacement_result)
