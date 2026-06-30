
import numpy as np

# making a 2x3 matrix
A = np.array([[1, 2, 3],
              [1, 2, 3]])

# printing its shape
print(np.shape(A))

print(A[1, 2])

B = np.array([[0, 2, 1],
              [2, 1, 3]])

Add_ab = A + B
print(Add_ab)

sub_ab = A - B
print(sub_ab)

print(5 * A)

# dot product of a and b throws in an error because again. columns on a should be equal to rows on b.
# print(np.dot(A, B))

matrix_A = np.array([[-1, 1, 2],
                     [3, -1, 1],
                     [-1, 3, 4]])

inverse_A = np.linalg.inv(matrix_A)
print(inverse_A)

det_A = np.linalg.det(matrix_A)
print(det_A)

# proof of inverse x original = identity

proof = matrix_A @ inverse_A
print(proof)

# or using the more efficient way and to avoid the point error

print(np.allclose(matrix_A @ inverse_A, np.eye(3)))



