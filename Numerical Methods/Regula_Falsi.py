import math

# Define the function
def f(x):
    return math.sqrt(x) - math.cos(x)

print("\nThe given equation is: sqrt(x) - cos(x) = 0.\n")

# Input: Interval [a, b] where f(a)*f(b) < 0
while True:
    a = float(input("Enter the left end point of the interval: "))
    b = float(input("Enter the right end point of the interval: "))
    y0 = f(a)
    y1 = f(b)

    if y0 == 0:
        print(f"\nA root of the given equation is {a}")
        exit()
    if y1 == 0:
        print(f"\nA root of the given equation is {b}")
        exit()
    if y0 * y1 > 0:
        print(f"\nRegula-Falsi method cannot locate any root in the interval [{a}, {b}].")
        print("Restart the method by putting new initial guesses.\n")
    else:
        break

# Input: Maximum iterations and tolerance
N = int(input("\nEnter the maximum number of iterations: "))
eps = float(input("Enter the tolerance (e.g., 1e-6): "))

print("\nThe Regula-Falsi iterations are:\n")
print(f"{'k':>3} {'a_k':>12} {'b_k':>12} {'x_k':>12} {'f(x_k)':>14}")

# Regula-Falsi Iteration
for k in range(1, N+1):
    x = a - (y0 * (b - a)) / (y1 - y0)
    y = f(x)

    print(f"{k:>3} {a:12.6f} {b:12.6f} {x:12.6f} {y:14.9f}")

    if abs(y) < eps:
        print(f"\nA root of the given equation is approximately {x:.9f} (within tolerance).")
        break

    if y0 * y > 0:
        a = x
        y0 = y
    else:
        b = x
        y1 = y
else:
    print(f"\nMaximum number of iterations reached.")
    print(f"An approximate root of the given equation is {x:.9f}.")

