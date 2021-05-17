import numpy as np

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