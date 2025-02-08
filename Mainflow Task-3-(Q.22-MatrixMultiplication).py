# ---6. : Multiply two matrices AAA and BBB.

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication not possible. Number of columns in A must equal number of rows in B.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [[1, 2, 3],  
     [4, 5, 6]]

B = [[7, 8],  
     [9, 10],  
     [11, 12]]

result_matrix = multiply_matrices(A, B)

if result_matrix:
    for row in result_matrix:
        print(row)
