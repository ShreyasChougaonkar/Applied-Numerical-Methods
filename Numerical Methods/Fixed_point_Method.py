import math

# Define the iteration function g(x)
# g = lambda x: (10/x - 4*x)**0.5
# g = lambda x: ((10 - x**3)/2)**0.5
# g = lambda x: math.sqrt(10 / (4 + x))
g = lambda x: math.sqrt(10 / (4 + x))  # ← you can switch g(x) here

print("\nThe given equation is: x^3 + 4x^2 - 10 = 0\n")

# Initial approximation
x0 = float(input("Enter the first initial approximation: "))

# Stopping criteria
N = int(input("Enter the maximum number of iterations: "))
eps = float(input("Enter the measure of accuracy (e.g., 1e-6): "))

# Header for iteration display
print("\nThe Fixed-point iterations are given as:\n")
print(f"{'k':>5} {'x_k':>14} {'g(x_k)':>14}")

# Print initial guess
gx = g(x0)
print(f"{1:>5} {x0:14.10f} {gx:14.10f}")

# Start iteration
p = 1
for k in range(2, N + 2):
    x = g(x0)
    gx = g(x)
    print(f"{k:>5} {x:14.10f} {gx:14.10f}")

    if abs(x - x0) <= eps:
        print(f"\nAn approximate solution (with tolerance {eps}) is {x:.10f}")
        p = 0
        break

    x0 = x

if p == 1:
    print(f"\nMaximum number of iterations reached. The method failed after {N} iterations.")
