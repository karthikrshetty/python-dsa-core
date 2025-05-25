"""
array_operations.py

Common operations: insert, delete, traverse in a Python list.
"""

def insert_element(arr, index, value):
    """Insert value at a given index"""
    arr.insert(index, value)
    return arr

def delete_element(arr, value):
    """Delete first occurrence of value"""
    if value in arr:
        arr.remove(value)
    return arr

def traverse_array(arr):
    """Print all elements"""
    for i in arr:
        print(i)

# Example usage
if __name__ == "__main__":
    nums = [10, 20, 30]
    nums = insert_element(nums, 1, 15)
    nums = delete_element(nums, 20)
    traverse_array(nums)
