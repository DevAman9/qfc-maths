import numpy as np

A = np.array([
    [ 0,  2, -3],
    [-2,  0,  4],
    [ 3, -4,  0]
])

print(f"determinant of matrix A: {np.linalg.det(A)}")

# inversing will throw in errors since the determinant is 0
# inverse_A = np.linalg.inv(A)

def is_skew_symmetric(matrix):
    transpose = matrix.T
    print(transpose)
    negative = -matrix
    print(negative)
    return np.array_equal(transpose, negative)

print("Is A skew-symmetric?", is_skew_symmetric(A))

def get_trace(matrix):
    return np.trace(matrix)

print (f"the trace of matrix A is {get_trace(A)}")


def get_rank(matrix):
    return np.linalg.matrix_rank(matrix)

print("Rank of A:", get_rank(A))

# rank means the number of independent (unique) rows in a matrix

B = np.array([
    [1, 2],
    [3, 4]
])

print("\n--- Testing Matrix B ---")
print("Is B skew-symmetric?", is_skew_symmetric(B))
print("Trace of B:", get_trace(B))
print("Rank of B:", get_rank(B))