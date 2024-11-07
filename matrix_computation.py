import numpy as np

def matrix_computation(A, B):
    # Compute the sum of A and B
    A_plus_B = A + B

    # Compute the difference of A and B
    A_minus_B = A - B

    # Compute the product of A and B
    A_times_B = A @ B

    # Compute the transpose of A
    A_transpose = A.T

    # Compute the inverse of A
    A_inverse = np.linalg.inv(A)

    return A_plus_B, A_minus_B, A_times_B, A_transpose