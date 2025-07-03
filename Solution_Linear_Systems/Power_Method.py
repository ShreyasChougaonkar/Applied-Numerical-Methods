import numpy as np

print("\nPower Method for Dominant Eigenvalue and Eigenvector")

# === User Input ===
n = int(input("\nEnter the dimension of the square matrix: "))
print("Enter the entries of the matrix row-wise:")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
A = np.array(A)

x = np.array(list(map(float, input("\nEnter an initial guess (column vector): ").split()))).reshape(n, 1)
TOL = float(input("\nEnter the tolerance: "))
N = int(input("Enter the maximum number of iterations: "))

print("\nThe given matrix is:")
print(A)

# === Find initial pivot index ===
p = np.argmax(np.abs(x))

# === Iteration Setup ===
z = x.copy()
Mu = []
k = 1

while k <= N:
    y = A @ x
    mu = y[p][0]
    Mu.append(mu)

    # Update pivot index based on max component in y
    p = np.argmax(np.abs(y))

    if y[p][0] == 0:
        print("\nAn eigenvector is:")
        print(x)
        print("0 is an eigenvalue.")
        break

    ERR = np.linalg.norm(x - y / y[p][0], ord=np.inf)
    x = y / y[p][0]
    z = np.hstack((z, x))

    if ERR < TOL:
        print(f"\nAn approximation of the dominant eigenvalue is: {mu:.6f}")
        print("An eigenvector corresponding to the dominant eigenvalue is:\n")
        print(x)
        break

    k += 1

# === Output Iterations ===
print("\nThe iterations for eigenvectors are given as (columns):")
print(np.round(z, 6))

print("\nThe iterations for eigenvalues are:")
print(np.round(Mu, 6))

if ERR >= TOL:
    print(f"\nAfter {N} iterations, the last approximation of dominant eigenvalue is: {mu:.2f}")
    print("\nEigenvector corresponding to the last approximation is:\n")
    print(x)
