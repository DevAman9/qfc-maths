from typing import final

import numpy as np



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