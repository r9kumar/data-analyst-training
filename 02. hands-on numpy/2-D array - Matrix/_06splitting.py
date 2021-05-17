import numpy as np

# <<<<<< splitting
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(np.array_split(arr, 3))
print(np.array_split(arr, 3, axis=1))
#print(np.hsplit(arr, 3))
#print(np.vsplit(arr, 3))
#print(np.dsplit(arr, 3))