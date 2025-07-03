import math

# Define the function and its derivative
def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

print("\nThe given equation is: x - cos(x) = 0\n")

# Input initial approximation
while True:
    try:
        x0 = float(input("Enter the first initial approximation: "))
        if f(x0) == 0:
            print(f"\nA root of the given equation is {x0:.10f}")
            exit()
        if df(x0) == 0:
            print("\nNewton-Raphson method cannot locate any root for the given equation.")
            print("Restart the method by putting new initial guesses.\n")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Input stopping criteria
N = int(input("\nEnter the maximum number of iterations: "))
eps = float(input("Enter the measure of accuracy (e.g., 1e-6): "))

# Header for iteration output
print("\nThe Newton-Raphson iterations are given as:\n")
print(f"{'k':>5} {'x_k':>14} {'f(x_k)':>14}")

# Print initial approximation
print(f"{0:>5} {x0:14.10f} {f(x0):14.10f}")

# Start iterations
for k in range(1, N + 1):
    if df(x0) == 0:
        print(f"\nThe method failed because df({x0:.10f}) = 0.")
        break

    x = x0 - f(x0) / df(x0)
    fx = f(x)

    print(f"{k:>5} {x:14.10f} {fx:14.10f}")

    if abs(fx) < eps:
        print(f"\nA root of the given equation is approximately {x:.10f} (within tolerance).")
        break

    if abs(x - x0) <= eps:
        print(f"\nAn approximate root (with tolerance {eps}) is {x:.10f}.")
        break

    x0 = x
else:
    print(f"\nMaximum number of iterations reached. The method failed after {N} iterations.")
