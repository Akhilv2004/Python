import numpy as np

array1 = np.random.randint(0, 21, size=(3, 3))
array2 = np.random.randint(0, 21, size=(3, 3))

matrix_addition = array1 + array2
matrix_multiplication = np.dot(array1, array2)
transpose_product = matrix_multiplication.T

print("Matrix 1:\n", array1)
print("Matrix 2:\n", array2)
print("Matrix Addition:\n", matrix_addition)
print("Matrix Multiplication:\n", matrix_multiplication)
print("Transpose of Product Matrix:\n", transpose_product)
