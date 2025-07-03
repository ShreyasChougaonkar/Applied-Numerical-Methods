import math

# Define the function
def f(x):
    return x - math.cos(x)

print("\nThe given equation is: x - cos(x) = 0\n")

# Initial guesses input loop
while True:
    try:
        x0 = float(input("Enter the first initial approximation: "))
        x1 = float(input("Enter the second initial approximation: "))
        y0 = f(x0)
        y1 = f(x1)

        if y0 == 0:
            print(f"\nA root of the given equation is {x0:.10f}")
            exit()
        if y1 == 0:
            print(f"\nA root of the given equation is {x1:.10f}")
            exit()
        if y0 == y1:
            print("\nSecant method cannot locate any root for the given equation.")
            print("Restart the method by putting new initial guesses.\n")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Get stopping criteria
N = int(input("\nEnter the maximum number of iterations: "))
eps = float(input("Enter the measure of accuracy (e.g., 1e-6): "))

print("\nThe Secant iterations are given as:\n")
print(f"{'k':>5} {'x_k':>14} {'f(x_k)':>14}")

# Print first two approximations
print(f"{1:>5} {x0:14.10f} {y0:14.10f}")
print(f"{2:>5} {x1:14.10f} {y1:14.10f}")

# Begin iterations
for k in range(3, N + 3):
    if (y1 - y0) == 0:
        print("\nDivision by zero in Secant formula — method fails.")
        break

    x = x1 - (y1 * (x1 - x0)) / (y1 - y0)
    y = f(x)

    print(f"{k:>5} {x:14.10f} {y:14.10f}")

    if abs(y) < eps:
        print(f"\nA root of the given equation is approximately {x:.10f} (f(x) ≈ 0).")
        break

    if abs(x - x1) <= eps:
        print(f"\nAn approximate root (with tolerance {eps}) is {x:.10f}.")
        break

    # Update for next iteration
    x0, y0 = x1, y1
    x1, y1 = x, y
else:
    print(f"\nMaximum number of iterations reached. The method failed after {N} iterations.")
