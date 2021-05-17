import numpy as np

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