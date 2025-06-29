import numpy as np
# Basic Operations on 2D Arrays

# Array Addition
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
result = x+y
print(result)

# Scalar Multiplication
z = np.array([[1,2],[3,4]])
result = z*2
print(result)

# Element-wise Multiplication (Hadamard Product)
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
result = x*y
print(result)

# Matrix Multiplication - Dot 
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
result = np.dot(A,B)
print(result)

# Get the transposed 
print(B.T)