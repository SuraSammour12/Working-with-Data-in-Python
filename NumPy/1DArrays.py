# One-Dimensional NumPy Arrays (1D Arrays)
import numpy as np
# Convert a Python list into a NumPy array
a = np.array([10,20,30,40])
print(a)
print(type(a)) # <class 'numpy.ndarray'>
print(a.dtype) # int64 (or float64 if using floats)

# Array Attributes
print(a.size) # number of elements
print(a.ndim) # number of dimensions
print(a.shape) # shape of array

# Indexing and Slicing
# Access or change an element by index
print(a[0])
a[2]=50
print(a)

# Slicing
# create a new array with elements at index 1, 2, 3
d = a[1:4]
print(d)


