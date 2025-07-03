import numpy as np

def doolittle_lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    z = 0

    print("\nGiven matrix is:")
    print(A)

    # Step-1
    if A[0, 0] == 0:
        print("Factorization is not possible (zero pivot).")
        return None, None

    U[0, 0] = A[0, 0]
    for j in range(1, n):
        # Step-2
        U[0, j] = A[0, j] / L[0, 0]
        L[j, 0] = A[j, 0] / U[0, 0]

    # Step-3
    for i in range(1, n - 1):
        # Step-4
        s = sum(L[i, k] * U[k, i] for k in range(i))
        U[i, i] = (A[i, i] - s) / L[i, i]

        if U[i, i] == 0:
            print(f"Factorization is not possible due to zero pivot at row {i+1}.")
            return None, None

        # Step-5
        for j in range(i + 1, n):
            r = sum(L[i, k] * U[k, j] for k in range(i))
            U[i, j] = (A[i, j] - r) / L[i, i]

            t = sum(L[j, k] * U[k, i] for k in range(i))
            L[j, i] = (A[j, i] - t) / U[i, i]

    # Step-6: Last diagonal entry of U
    w = sum(L[n - 1, k] * U[k, n - 1] for k in range(n - 1))
    U[n - 1, n - 1] = (A[n - 1, n - 1] - w) / L[n - 1, n - 1]

    print("\nDoolittle's LU decomposition of the given matrix:")
    print("\nMatrix L:")
    print(L)
    print("\nMatrix U:")
    print(U)

    return L, U


# === User Input ===
print("Doolittle's LU Decomposition")

n = int(input("Enter the dimension of the square matrix: "))
print(f"Enter the {n} x {n} matrix row-wise:")

a = []
for i in range(n):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    a.append(row)

A = np.array(a)

# Perform decomposition
L, U = doolittle_lu_decomposition(A)
