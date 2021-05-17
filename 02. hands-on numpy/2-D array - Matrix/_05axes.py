import numpy as np;

matrix = np.array([
  [5, 3, 7, 1],
  [2, 6, 7 ,9],
  [1, 1, 1, 1],
  [4, 3, 2, 0]
]);
print(matrix);

# <<<<<< axes [axis-1 = row and axis-0 = column]
print(matrix.max())
print(matrix.max(axis=0))
print(matrix.max(axis=1))

print(matrix.min())
print(matrix.min(axis=0))
print(matrix.min(axis=1))

print(np.mean(matrix))
print(np.mean(matrix, axis=0))
print(np.mean(matrix, axis=1))

print(np.var(matrix))
print(np.var(matrix, axis=0))
print(np.var(matrix, axis=1))

print(np.std(matrix))
print(np.std(matrix, axis=0))
print(np.std(matrix, axis=1))

print(np.sort(matrix))
print(np.sort(matrix,axis=0))
print(np.sort(matrix,axis=1))