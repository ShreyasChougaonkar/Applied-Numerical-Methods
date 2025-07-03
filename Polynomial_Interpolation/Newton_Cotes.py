def newton_cotes_closed(f, a, b, n):
    """
    Compute the definite integral of f from a to b using closed Newton–Cotes formulas
    Supported: n = 1 (Trapezoidal), 2 (Simpson), 3 (Simpson 3/8), 4 (Boole’s Rule)
    """
    if n not in [1, 2, 3, 4]:
        raise ValueError("Only n = 1, 2, 3, 4 supported (Trapezoidal to Boole's Rule)")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    print(f"\nUsing Newton–Cotes Rule with n = {n}")
    print("Sample points:")
    for i in range(n + 1):
        print(f"  x[{i}] = {x[i]:.6f}, f(x) = {y[i]:.6f}")

    if n == 1:
        # Trapezoidal Rule
        integral = (h / 2) * (y[0] + y[1])
    elif n == 2:
        # Simpson’s Rule
        integral = (h / 3) * (y[0] + 4 * y[1] + y[2])
    elif n == 3:
        # Simpson’s 3/8 Rule
        integral = (3 * h / 8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])
    elif n == 4:
        # Boole’s Rule
        integral = (2 * h / 45) * (7*y[0] + 32*y[1] + 12*y[2] + 32*y[3] + 7*y[4])

    print(f"\nApproximate integral value: {integral:.8f}")
    return integral


# === User Input ===
import math

print("\nClosed Newton–Cotes Numerical Integration\n")

# Define the function to integrate
# f = lambda x: math.sin(x)
f = lambda x: x**3 + 2*x**2 + 1  # Example polynomial

a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter n (1=Trapezoidal, 2=Simpson, 3=3/8 Rule, 4=Boole): "))

# === Compute Integral ===
newton_cotes_closed(f, a, b, n)
