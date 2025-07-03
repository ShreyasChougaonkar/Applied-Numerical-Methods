import numpy as np

def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n, n))

    print("\nPerforming Cholesky Decomposition...\n")
    
    for i in range(n):
        for j in range(i + 1):
            sum_ = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                val = A[i][i] - sum_
                if val <= 0:
                    raise ValueError("Matrix is not positive definite.")
                L[i][j] = np.sqrt(val)
            else:
                L[i][j] = (A[i][j] - sum_) / L[j][j]

    print("Matrix L (lower triangular):\n")
    print(np.round(L, 6))

    print("\nMatrix L^T (upper triangular):\n")
    print(np.round(L.T, 6))

    print("\nReconstructed A = L * L^T:\n")
    print(np.round(L @ L.T, 6))

    return L


# === User Input ===
print("Cholesky Decomposition (for symmetric positive definite matrices)")

n = int(input("\nEnter the dimension of the square matrix: "))
print("Enter the entries of the matrix row-wise (symmetric):")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
A = np.array(A)

# Check if symmetric
if not np.allclose(A, A.T):
    raise ValueError("Matrix is not symmetric.")

# Perform Cholesky decomposition
L = cholesky_decomposition(A)
