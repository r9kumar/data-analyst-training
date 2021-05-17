import numpy as np;

# Create matrix_a
matrix_a = np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 2]
])
print(matrix_a);

# Create matrix_b
matrix_b = np.array([
  [1, 3, 1],
  [1, 3, 1],
  [1, 3, 8]
])
print(matrix_b);

# <<<<<< matrix operation

# Add two matrices
print(np.add(matrix_a, matrix_b))

# Subtract two matrices
print(np.subtract(matrix_a, matrix_b))

# Multiply two matrices element-wise
print(matrix_a * matrix_b)

# Multiply two matrices
print(np.dot(matrix_a, matrix_b))

# non-singular matrix
matrix = np.array([
  [5, 3, 7, 1],
  [2, 6, 7 ,9],
  [1, 1, 1, 1],
  [4, 3, 2, 0]
]);
print(matrix);

# singular matrix
smatrix = np.array([
  [1, 2, 3],
  [2, 4, 6],
  [3, 8, 9]
])
print(smatrix);

# <<<<<< matrix operation

print(matrix.clip(2,3));
print(matrix.cumsum(axis=0));

# Return diagonal elements
print(matrix.diagonal())
print(np.diag(matrix))

# Return diagonal one above the main diagonal
print(matrix.diagonal(offset=1))

# Return diagonal one below the main diagonal
print(matrix.diagonal(offset=-1))

# Return trace
print(matrix.trace())

# Return transpose
print(matrix.transpose())
print(matrix.T)
print(np.transpose(matrix))

# Return determinant of matrix
print(np.linalg.det(matrix))

# Return matrix rank
print(np.linalg.matrix_rank(matrix))

# Calculate inverse of matrix
print(np.linalg.inv(matrix))

# Covariance Matrix 

# Correlation Matrix

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)

# <<<<<< SINGULAR VALUE DECOMPOSITION
#Creating a matrix A
A = np.array([[3,4,3],[1,2,3],[4,2,1]])

#Performing SVD
U, D, VT = np.linalg.svd(A)

#Checking if we can remake the original matrix using U,D,VT
A_remake = (U @ np.diag(D) @ VT)
print(A_remake)

# <<<<<< matrix or vector norm

# EXAMPLE-01
u = np.array([1, 6])
v = np.array([4, 2])
print(u+v)
print(np.linalg.norm(u+v))
print(np.linalg.norm(u)+np.linalg.norm(v))

# EXAMPLE-02
# initialize matrix
mat = np.array([
  [ 1, 2, 3],
  [4, 5, 6]
])
# compute norm of matrix
mat_norm = np.linalg.norm(mat)
print(mat_norm)
# compute matrix num along axis 
print(np.linalg.norm(mat, axis = 1))

# EXAMPLE-03
# initialze vector
vec = np.arange(9)
# convert vector into matrix
mat = vec.reshape((3, 3))
# compute norm of vector
print(np.linalg.norm(vec)) 
# computer norm of matrix
print(np.linalg.norm(mat))