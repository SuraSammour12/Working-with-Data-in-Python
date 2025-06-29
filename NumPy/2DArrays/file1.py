a = [[11,12,13],[21,22,23],[31,32,33]]
import numpy as np
array = np.array(a)
print(array)

# Numpy Array Attributes
# ndim : number of dimensions or axes
print(array.ndim) # 2D array
# shape : returns a tuple representing the dimensions of the array
print(array.shape)
# size : total number of elements in the array
print(array.size)

# Indexing and slicing in 2D Arrays
# Indexing
print(array[1,2])
# Slicing 
# To get the first two rows and the first two columns:
print(array[:2,:2])
# To get the last column for all rows
print(array[:,2])