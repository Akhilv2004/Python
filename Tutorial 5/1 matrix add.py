import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

result = matrix1 + matrix2
transpose_result = result.T

print("Resultant Matrix:")
print(result)

print("Transpose of the Resultant Matrix:")
print(transpose_result)
