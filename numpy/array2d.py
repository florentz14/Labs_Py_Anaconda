import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:")
print(matrix)

# Matrix operations
print("\nTranspose:")
print(matrix.T)

print("\nSum of all elements:", np.sum(matrix))
print("Sum along rows:", np.sum(matrix, axis=1))
print("Sum along columns:", np.sum(matrix, axis=0))

# Matrix multiplication
vector = np.array([1, 2, 3])
result = np.dot(matrix, vector)
print("\nMatrix-vector multiplication result:", result)
