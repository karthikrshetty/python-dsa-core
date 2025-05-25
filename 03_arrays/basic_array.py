"""
basic_array.py

Simple usage of Python's built-in list as a dynamic array.
"""

# Create a list
arr = [10,20,30,40]

#Accessing elements
print("First element:", arr[0])  # Output: 10

#Modifying elements
arr[1] = 25
print("Modified second element:", arr[1])  # Output: 25

#Adding elements
arr.append(50) #add at end
arr.insert(2,25) #add at index 2
print("Array after adding elements:", arr)  # Output: [10, 25, 25, 30, 40, 50]

#Removing elements
arr.remove(25)  # remove first occurrence of 25
deleted_element = arr.pop(3)  # remove element at index 3
print("Deleted element:", deleted_element)  # Output: 30
print("Array after removing elements:", arr)  # Output: [10, 25, 30, 40, 50]


#iterating through the array
for item in arr:
    print("Item:", item)

#length of the array
print("Length of array:", len(arr))  # Output: 5