#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Create a vector of length 5 with integers ranging from 0 to 10
v = np.random.randint(low=0, high=11, size=5)

# Print the vector
print(v)


# In[2]:


import numpy as np

# Create a vector with values ranging from 15 to 55
v = np.arange(start=15, stop=56)

# Print all values except the first and last
print(v[1:-1])


# In[3]:


import numpy as np

# Create a random array with 1000 elements
arr = np.random.rand(1000)

# Compute the average, variance, and standard deviation of the array elements
avg = np.mean(arr)
var = np.var(arr)
std_dev = np.std(arr)

# Print the results
print("Array Average:", avg)
print("Array Variance:", var)
print("Array Standard Deviation:", std_dev)


# In[4]:


import numpy as np

# Create a 3x3 array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the cumulative sum of the elements along the rows axis
cumulative_sum_rows = np.cumsum(arr, axis=0)

# Calculate the cumulative sum of the elements along the columns axis
cumulative_sum_cols = np.cumsum(arr, axis=1)

# Calculate the sum over rows for each of the 3 columns
sum_cols = np.sum(arr, axis=0)

# Calculate the sum over columns for each of the 2 rows
sum_rows = np.sum(arr, axis=1)

# Print the results
print("Original Array:\n", arr)
print("Cumulative Sum (Rows):\n", cumulative_sum_rows)
print("Cumulative Sum (Columns):\n", cumulative_sum_cols)
print("Sum Over Rows for Each Column:\n", sum_cols)
print("Sum Over Columns for Each Row:\n", sum_rows)


# In[5]:


import numpy as np

# Create the first matrix
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create the second matrix
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Compute the multiplication of the two matrices
result = np.dot(matrix1, matrix2)

# Print the result
print("Result:\n", result)


# In[ ]:




