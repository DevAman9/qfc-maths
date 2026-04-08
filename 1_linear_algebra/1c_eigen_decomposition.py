


import numpy as np


matrix_A = np.array([
    [4, 5, 6],
    [5, 4, 7],
    [6, 7, 4]
])

matrix_At = matrix_A.T
print(matrix_At)

print(np.array_equal(matrix_A, matrix_At))

eigen_A = np.linalg.eig(matrix_A)
print(eigen_A)

# output results from the above.
# True
# EigResult(eigenvalues=array([16.03711293, -0.86489524, -3.17221769]),
# eigenvectors=array([[ 0.54345816,  0.80596883, -0.23466457],
#        [ 0.57912577, -0.56235096, -0.59023278],
#        [ 0.60767307, -0.18486652,  0.77237155]]))

# Eigen values are the lambda values in the function (A - 𝜆I) = 0
# They represent the magnitude of eigenvectors after a matrix has been applied onto the space.
# Eigen vectors are in the form [x, y , z] for a 3x3 matrix.

V = np.linalg.eig(matrix_A).eigenvectors

eigenvalues = np.linalg.eig(matrix_A).eigenvalues

Lambda = np.diag(eigenvalues)
print(f"Matrix with eigenvalues in the diagonal:\n {Lambda}")

V_inv = np.linalg.inv(V)

reconstructed_A = V @ Lambda @ V_inv
print("Reconstructed Matrix:\n", reconstructed_A)

# This outputs the same result as the original matrix

