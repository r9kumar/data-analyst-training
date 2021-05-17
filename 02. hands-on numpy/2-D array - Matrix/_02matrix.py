import numpy as np;

matrix = np.array([
  [5, 3, 7, 1],
  [2, 6, 7 ,9],
  [1, 1, 1, 1],
  [4, 3, 2, 0]
]);
print(matrix);
"""
#Describing a Matrix
print(matrix.ndim);
print(matrix.dtype);
print(matrix.shape);
print(matrix.size)
print(matrix.astype('f'));
"""

# <<<<<< indexing
print(matrix[0])
print(matrix[1:2,0:2])
# Select the first two rows and all columns of a matrix
print(matrix[:2,:])
# Select all rows and the second column
print(matrix[:,1:2])

# <<<<<< axes
print(matrix.max())
print(matrix.max(axis=0))
print(matrix.max(axis=1))

# <<<<<< reshaping
temperatures = np.array([29.3, 42.1, 18.8, 16.1, 38.0, 12.5,12.6, 49.9, 38.6, 31.3, 9.2, 22.2]).reshape(2, 2, 3)
print(temperatures.shape)
print(np.swapaxes(temperatures, 1, 2))

# Create 4x3 matrix
matrix = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
])

# Reshape matrix into 2x6 matrix
print(matrix.reshape(2, 6))
print(matrix.reshape(1, -1))
print(matrix.reshape(12))
# Flatten matrix
print(matrix.flatten())

# <<<<<< joining
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.concatenate((arr1, arr2)))

#Join two 2-D arrays along rows (axis=1)
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2), axis=0))

print(np.stack((arr1, arr2), axis=1))
print(np.hstack((arr1, arr2)))
print(np.vstack((arr1, arr2)))
print(np.dstack((arr1, arr2)))

# <<<<<< splitting
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(np.array_split(arr, 3))
print(np.array_split(arr, 3, axis=1))
#print(np.hsplit(arr, 3))
#print(np.vsplit(arr, 3))
#print(np.dsplit(arr, 3))

# <<<<<< masking and filtering

# <<<<<< vectorization

# <<<<<< broadcasting
