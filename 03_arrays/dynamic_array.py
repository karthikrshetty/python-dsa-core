"""
dynamic_array.py

Custom dynamic array class that mimics array resizing (like ArrayList in Java).
"""

import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0 # Number of elements
        self.capacity = 1 #initial capacity
        self.A = self.__make_array(self.capacity) # Create an array with initial capacity

    def __len__(self):
        return self.n
    
    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError('Index out of bounds')
        return self.A[index]
    
    def append(self, item):
        if self.n == self.capacity:
            self.__resize(2 * self.capacity) # Double the capacity
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity) # Create a new array with new capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_capacity
    
    def __make_array(self, capacity):   
        """Create a new array with the given capacity."""
        return (capacity * ctypes.py_object)()

# Example usage
if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(5):
        arr.append(i * 10)
    for i in range(len(arr)):
        print(arr[i])


# ---

# ## ✅ Algorithm: Dynamic Array Creation and Append Operation

# ### Step 1: **Initialize the Array**

# * Set `n = 0` → number of actual elements
# * Set initial `capacity = 1`
# * Create a low-level array of size `capacity` using `ctypes`

# ---

# ### Step 2: **Append an Element**

# * If `n == capacity` (array is full):

#   * Go to **Step 3 (Resize)**
# * Insert the element at index `n`
# * Increment `n` by 1

# ---

# ### Step 3: **Resize the Array (When Full)**

# * Create a new array `B` with size `2 × capacity`
# * Copy all elements from old array `A` to new array `B`
# * Set `A = B` (replace reference)
# * Update `capacity = 2 × capacity`
# * Retry the append (now there is space)

# ---

# ### Step 4: **Access Elements**

# * Use `arr[i]` → calls `__getitem__`
# * Validate index `0 <= i < n`, return `A[i]`

# ---

# ### 🔁 These steps repeat as elements are added.

# ---

# ## 🎯 Key Properties:

# * **Dynamic resizing:** Capacity doubles when needed
# * **Efficient access:** O(1) random access
# * **Amortized O(1) append:** Even though resize is O(n), it happens rarely

# ---

# Would you like this visualized as a flowchart or pseudocode as well?
