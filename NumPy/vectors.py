# Basic Operation on Vectors
import numpy as np
u = np.array([1, 0])
v = np.array([0, 1])
# vector addition
z1 = u+v # [1, 1]
print(z1)
# vector subtraction
z2 = u-v
print(z2)
# scalar multiplication
y = np.array([1,2])
z3 = 2*y
print(z3)
# hadamard product (element-wise multiplication)
u1 = np.array([1,2])
v1 = np.array([3,4])
z4 = u1*v1
print(z4)
# Dot product
result = np.dot(u1,v1) # (3*1)+(2*4)
print(result)

# Broadcasing 
# Add a scalar to a NumPy array
a = np.array([1,2,3])
b = a+3 # [4,5,6]
print(b)

print('----------------------------------------------------------------------------')
# Universal Functions
# Function that operate on arrays element-wise
# Example: Mean and Max
a = np.array([-2,0,2])
print(a.mean())
print(a.max())
print('----------------------------------------------------------------------------')
# Math Functions with Arrays
# np.sin() | np.cos()
# Note : np.pi = π 
x = np.array([0, np.pi/2, np.pi]) # Vector
y = np.sin(x) # this apply the sine function to each element in the array
print(x)
print(y)
print('----------------------------------------------------------------------------')

# linspace: function for plotting mathematical function 
# linspace return evenly spaced numbers over a specified interval
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100) 
# 0: starting point of the sequence
# 2*np.pi: ending point of the sequence
# 100 : num : the number of samples to generate
y = np.sin(x)

plt.plot(x, y)
plt.show()