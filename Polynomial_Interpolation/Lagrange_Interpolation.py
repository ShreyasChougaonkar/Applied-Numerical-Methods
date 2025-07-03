def lagrange_interpolation(x_values, y_values, xp):
    """
    Lagrange Interpolation Formula:
    L(xp) = Σ y[i] * Π_{j≠i} (xp - x[j]) / (x[i] - x[j])
    """
    n = len(x_values)
    result = 0.0

    print("\nCalculating Lagrange Interpolation at x =", xp)
    print("\nEach L_i(x) term:")

    for i in range(n):
        term = y_values[i]
        Li_parts = []
        for j in range(n):
            if j != i:
                term *= (xp - x_values[j]) / (x_values[i] - x_values[j])
                Li_parts.append(f"(x - {x_values[j]}) / ({x_values[i]} - {x_values[j]})")
        print(f"L_{i}(x) = {' * '.join(Li_parts)} → contributes: {term:.6f}")
        result += term

    print(f"\nInterpolated value at x = {xp} is: {result:.6f}")
    return result


# === User Input ===
print("\nLagrange Interpolation Method\n")
n = int(input("Enter the number of data points: "))

x_vals = []
y_vals = []

print("\nEnter the data points (x, y):")
for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    x_vals.append(x)
    y_vals.append(y)

xp = float(input("\nEnter the value of x at which to interpolate: "))

# === Perform Interpolation ===
lagrange_interpolation(x_vals, y_vals, xp)
