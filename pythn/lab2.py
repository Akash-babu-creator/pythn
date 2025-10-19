def multiply_matrices(A, B):
    # Number of rows in A, columns in B
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Number of columns of A must equal number of rows of B")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]

    return result